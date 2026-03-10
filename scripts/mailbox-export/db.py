#!/usr/bin/env python3
"""
SQLite database setup and helper functions.
Single-file database for all mailboxes, messages, tags, and full-text search.
"""

import sqlite3
import json
import os
from config import DB_PATH


def get_db():
    """Get a database connection with WAL mode and foreign keys enabled."""
    db = sqlite3.connect(DB_PATH)
    db.execute("PRAGMA journal_mode=WAL")
    db.execute("PRAGMA foreign_keys=ON")
    db.row_factory = sqlite3.Row
    return db


def init_db():
    """Create all tables if they don't exist."""
    db = get_db()
    db.executescript("""

    CREATE TABLE IF NOT EXISTS mailboxes (
        id              INTEGER PRIMARY KEY AUTOINCREMENT,
        email           TEXT UNIQUE NOT NULL,
        display_name    TEXT,
        scanned_at      TIMESTAMP,
        total_messages  INTEGER DEFAULT 0
    );

    CREATE TABLE IF NOT EXISTS messages (
        id                  INTEGER PRIMARY KEY AUTOINCREMENT,
        mailbox_id          INTEGER NOT NULL REFERENCES mailboxes(id),
        graph_id            TEXT NOT NULL,

        subject             TEXT,
        sender_address      TEXT,
        sender_name         TEXT,
        to_recipients       TEXT,
        received_at         TIMESTAMP,
        importance          TEXT,
        is_read             BOOLEAN,
        has_attachments     BOOLEAN,
        has_list_headers    BOOLEAN,
        list_header_names   TEXT,
        internet_headers    TEXT,

        action              TEXT,
        llm_reason          TEXT,
        confidence          REAL,
        classified_at       TIMESTAMP,

        eml_path            TEXT,
        exported_at         TIMESTAMP,

        outlook_categories  TEXT,
        outlook_synced_at   TIMESTAMP,
        outlook_deleted_at  TIMESTAMP,

        UNIQUE(mailbox_id, graph_id)
    );

    CREATE TABLE IF NOT EXISTS tags (
        id              INTEGER PRIMARY KEY AUTOINCREMENT,
        message_id      INTEGER NOT NULL REFERENCES messages(id),
        tag             TEXT NOT NULL,
        confidence      REAL,
        llm_reason      TEXT,

        UNIQUE(message_id, tag)
    );

    CREATE INDEX IF NOT EXISTS idx_messages_mailbox   ON messages(mailbox_id);
    CREATE INDEX IF NOT EXISTS idx_messages_action    ON messages(action);
    CREATE INDEX IF NOT EXISTS idx_messages_sender    ON messages(sender_address);
    CREATE INDEX IF NOT EXISTS idx_messages_received  ON messages(received_at);
    CREATE INDEX IF NOT EXISTS idx_tags_tag           ON tags(tag);
    CREATE INDEX IF NOT EXISTS idx_tags_message       ON tags(message_id);

    CREATE VIRTUAL TABLE IF NOT EXISTS messages_fts USING fts5(
        subject,
        sender_address,
        sender_name,
        body_text,
        content=messages,
        content_rowid=id
    );

    """)
    db.commit()
    db.close()
    print(f"Database initialized: {os.path.abspath(DB_PATH)}")


def get_or_create_mailbox(db, email, display_name):
    """Get or create a mailbox row, return its id."""
    row = db.execute(
        "SELECT id FROM mailboxes WHERE email = ?", (email,)
    ).fetchone()
    if row:
        return row["id"]
    cursor = db.execute(
        "INSERT INTO mailboxes (email, display_name) VALUES (?, ?)",
        (email, display_name)
    )
    db.commit()
    return cursor.lastrowid


def upsert_message(db, mailbox_id, graph_id, metadata):
    """Insert or update a message. Returns the message row id."""
    existing = db.execute(
        "SELECT id FROM messages WHERE mailbox_id = ? AND graph_id = ?",
        (mailbox_id, graph_id)
    ).fetchone()

    if existing:
        db.execute("""
            UPDATE messages SET
                subject = ?, sender_address = ?, sender_name = ?,
                to_recipients = ?, received_at = ?, importance = ?,
                is_read = ?, has_attachments = ?, has_list_headers = ?,
                list_header_names = ?, internet_headers = ?
            WHERE id = ?
        """, (
            metadata["subject"], metadata["sender_address"],
            metadata["sender_name"], metadata["to_recipients"],
            metadata["received_at"], metadata["importance"],
            metadata["is_read"], metadata["has_attachments"],
            metadata["has_list_headers"],
            json.dumps(metadata.get("list_header_names", [])),
            json.dumps(metadata.get("internet_headers", [])),
            existing["id"]
        ))
        return existing["id"]
    else:
        cursor = db.execute("""
            INSERT INTO messages (
                mailbox_id, graph_id, subject, sender_address, sender_name,
                to_recipients, received_at, importance, is_read,
                has_attachments, has_list_headers, list_header_names,
                internet_headers
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            mailbox_id, graph_id,
            metadata["subject"], metadata["sender_address"],
            metadata["sender_name"], metadata["to_recipients"],
            metadata["received_at"], metadata["importance"],
            metadata["is_read"], metadata["has_attachments"],
            metadata["has_list_headers"],
            json.dumps(metadata.get("list_header_names", [])),
            json.dumps(metadata.get("internet_headers", [])),
        ))
        return cursor.lastrowid


def set_classification(db, message_id, action, reason, confidence, tags):
    """Store LLM classification results for a message."""
    from datetime import datetime
    db.execute("""
        UPDATE messages SET action = ?, llm_reason = ?, confidence = ?,
        classified_at = ? WHERE id = ?
    """, (action, reason, confidence, datetime.utcnow().isoformat(), message_id))

    db.execute("DELETE FROM tags WHERE message_id = ?", (message_id,))
    for t in tags:
        db.execute("""
            INSERT OR IGNORE INTO tags (message_id, tag, confidence, llm_reason)
            VALUES (?, ?, ?, ?)
        """, (message_id, t["tag"], t.get("confidence"), t.get("reason")))

    db.commit()


def get_stats(db):
    """Print summary statistics."""
    for row in db.execute("""
        SELECT mb.display_name, mb.email,
               COUNT(*) as total,
               SUM(CASE WHEN m.action = 'KEEP' THEN 1 ELSE 0 END) as kept,
               SUM(CASE WHEN m.action = 'SPAM' THEN 1 ELSE 0 END) as spam,
               SUM(CASE WHEN m.action = 'NEWSLETTER' THEN 1 ELSE 0 END) as newsletter,
               SUM(CASE WHEN m.action IS NULL THEN 1 ELSE 0 END) as unclassified
        FROM messages m
        JOIN mailboxes mb ON mb.id = m.mailbox_id
        GROUP BY mb.id
    """).fetchall():
        print(f"  {row['display_name']:20s}  total={row['total']:5d}  "
              f"keep={row['kept']:5d}  spam={row['spam']:5d}  "
              f"newsletter={row['newsletter']:5d}  "
              f"unclassified={row['unclassified']:5d}")

    print("\n  Tag distribution:")
    for row in db.execute("""
        SELECT t.tag, COUNT(*) as count
        FROM tags t GROUP BY t.tag ORDER BY count DESC
    """).fetchall():
        print(f"    {row['tag']:12s}  {row['count']:5d}")


if __name__ == "__main__":
    init_db()
