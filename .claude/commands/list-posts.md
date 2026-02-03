# List Posts

List all marketing posts, optionally filtered by status.

## Usage
`/list-posts [status]`

## Examples
- `/list-posts` - List all posts
- `/list-posts draft` - List only draft posts
- `/list-posts published` - List only published posts

## Instructions
When the user invokes this command:
1. Search for all `post.md` files in the `posts/` directory
2. Extract metadata from each post:
   - Title (first `# ` heading)
   - Status (from the metadata bullet `- **Status**: ...`)
   - Date (from directory path)
3. If a status filter is provided, only show posts matching that status
4. Display results in a readable format with:
   - Post path/name
   - Title
   - Status
   - Date

Status values: `draft`, `in_review`, `approved`, `published`
