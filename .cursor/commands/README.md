# Cursor Slash Commands

These commands work in Cursor's chat interface. Type `/` followed by the command name.

## Available Commands

- `/new-post` - Create a new marketing post
- `/list-posts` - List all posts (optionally filtered by status)
- `/update-status` - Update a post's status

## Adding New Commands

Create a new `.md` file in `.cursor/commands/` with:
1. A title (becomes the command name)
2. Usage instructions
3. Examples
4. Detailed instructions for the AI agent

The filename becomes the command name (e.g., `new-post.md` → `/new-post`).
