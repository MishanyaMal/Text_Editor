# Text Editor App

A lightweight desktop-style text editor for creating, opening, and editing plain text files. Files are stored in a local `notes` folder and can be accessed via the sidebar panel.

## Key Features

- **Create New Files:** Start a new text document with a single click.
- **Open Existing Files:** Browse and open any `.txt` file from the `notes` folder.
- **Edit Text:** Real‑time editing with a clean, distraction‑free interface.
- **Save Changes:** Automatically saves to the original file or lets you save as a new file.
- **File Browser:** Sidebar panel displays all available `.txt` files in the `notes` folder. Click to open.
- **Auto‑Refresh:** The file list updates automatically when files are added or removed from the `notes` folder.

## Technologies Used

- **Language:** 'Python'
- **Core Modules:** `os`, `sys` (for file system operations)
- **Main Python Module:** 'PyQt6'

## How It Works

1. On launch, the app scans the local `notes` folder and populates the sidebar with all `.txt` files.
2. Clicking a file in the sidebar loads its content into the editor.
3. Edits are reflected instantly. Changes can be saved back to the same file or exported as a new one.
4. New files can be created and saved directly to the `notes` folder.
