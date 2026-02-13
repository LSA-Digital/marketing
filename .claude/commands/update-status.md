# Update Status

Update the status of a marketing post.

## Usage
`/update-status <post-path> <new-status>`

## Examples
- `/update-status posts/2026/02/2026-02-03_2026-B-001_lsars/post.md approved`
- `/update-status posts/2026/02/2026-02-15_2026-T-002_epms/post.md published`

## Instructions
When the user invokes this command:
1. Read the specified post file
2. Find the metadata bullet line starting with `- **Status**:` in the metadata section
3. Update it to the new status value
4. Update /post-index.md with same status for this post
4. Save the file
5. Confirm the update
6. git commit / push changes

Valid status values: `draft`, `in_review`, `approved`, `published`, `rejected`
