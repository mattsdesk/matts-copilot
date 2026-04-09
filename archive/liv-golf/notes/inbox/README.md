# Inbox

Drop emails and attachments here to have them automatically processed into the notes repo.

## How to use

1. **Drag an email** from Outlook into this folder (saves as `.eml`) — or use File → Save As to save as `.txt` or `.msg`
2. **Drop any attachments** into this folder alongside the email (`.pdf`, `.docx`, `.pptx`, `.xlsx`, images)
3. That's it — the next morning sync will pick everything up, update the relevant project docs and TODO.md, then move the files to `processed/`

## What gets processed

- `.eml` — dragged emails from Outlook (recommended)
- `.msg` — Outlook message files
- `.txt` — plain text email bodies
- `.pdf` — PDF attachments or documents
- `.docx` — Word documents
- `.pptx` — PowerPoint decks
- `.xlsx` — spreadsheets
- Images (`.png`, `.jpg`) — screenshots, scanned docs

## What happens after processing

Files are moved to `inbox/processed/` with a timestamp prefix so you have a record of what was ingested. Nothing is ever deleted.

## Tips

- You can drop multiple emails and attachments at once — they'll all be processed in the next sync
- If an email is clearly about a new topic not covered by existing projects, a new project doc will be created automatically
- If you want something processed immediately rather than waiting for the morning sync, you can trigger the scheduled task manually from the Claude sidebar
