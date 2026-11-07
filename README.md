# Smart File Organizer

A Python-based file organization tool that automatically scans folders, categorizes files by their extensions, and organizes them into separate folders.

## Features

- **Automatic File Categorization:** Sorts files into categories based on their extensions.
- **Recursive Scanning:** Scans files inside subfolders as well.
- **Dry Run Mode:** Previews planned file movements before making changes.
- **Duplicate Handling:** Prevents overwriting existing files by generating unique filenames.
- **Unknown File Handling:** Places unsupported file types into an `Others` folder.
- **Extension Normalization:** Converts file extensions to lowercase.
- **Safe Organization:** Skips files that are already in their correct category folders.
- **File Information:** Displays file names, extensions, sizes, modification dates, and categories.

## Supported Categories

| Category | Extensions |
|---|---|
| Images | `.jpg`, `.jpeg`, `.png`, `.gif`, `.svg` |
| Documents | `.pdf`, `.docx`, `.doc`, `.txt`, `.pptx`, `.xlsx` |
| Videos | `.mp4`, `.mkv`, `.avi`, `.mov` |
| Audio | `.mp3`, `.wav`, `.aac`, `.flac` |
| Code | `.py`, `.c`, `.h`, `.java`, `.cpp`, `.js`, `.html`, `.css` |
| Archives | `.zip`, `.rar`, `.7z`, `.tar` |
| Others | Unsupported extensions |

## Project Structure

```text
Smart_File_Organizer/
│
├── main.py
├── file_scanner.py
├── organizer.py
├── README.md
├── .gitignore
└── requirements.txt
```

## Technologies Used

- Python 3.13
- pathlib
- shutil
- datetime

## How to Run

1. Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
```

2. Navigate into the project folder:

```bash
cd Smart_File_Organizer
```

3. Run the application:

```bash
python main.py
```

4. Enter the folder path you want to organize.

5. Review the dry-run preview.

6. Enter `yes` or `y` to proceed with file organization.

## How It Works

1. The user provides a folder path.
2. The scanner recursively scans the directory and collects file information.
3. Each file is assigned a category based on its extension.
4. The organizer generates a preview of the planned movements.
5. After user confirmation, files are moved into their respective category folders.
6. Duplicate filenames are handled by generating unique names.

## Future Improvements

- Logging and activity tracking.
- Backup and restore functionality.
- Undo file organization.
- Configuration through a separate settings file.
- Automated unit testing.

## Author

Navaneet Upadhyay