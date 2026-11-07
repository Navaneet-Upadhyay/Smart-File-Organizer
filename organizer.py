import shutil
from pathlib import Path

categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Code": [".py", ".c", ".h", ".java", ".cpp", ".js", ".html", ".css"],
    "Archives": [".zip", ".rar", ".7z", ".tar"],
}


def get_category(extension):
    extension = extension.lower()

    for category, extensions in categories.items():
        if extension in extensions:
            return category

    return "Others"


def get_unique_path(destination_path):
    destination_path = Path(destination_path)

    if not destination_path.exists():
        return destination_path

    counter = 1

    while True:
        new_name = f"{destination_path.stem}_{counter}{destination_path.suffix}"

        new_path = destination_path.parent / new_name

        if not new_path.exists():
            return new_path

        counter += 1


def organize_files(files, source_folder, dry_run=True):
    moved = 0
    skipped = 0
    planned = 0

    source_folder = Path(source_folder)

    for item in files:
        file_name = item["name"]
        category = item["category"]

        source_path = source_folder / item["relative_path"]
        destination_folder = source_folder / category

        file_path = Path(file_name)
        new_name = file_path.stem + file_path.suffix.lower()

        if not source_path.exists():
            print(f"Source file not found: {file_name}")
            skipped += 1
            continue

        # Skip files already in their correct category folder
        current_folder = Path(item["relative_path"]).parent

        if (
            len(current_folder.parts) == 1
            and current_folder.name.lower() == category.lower()
        ):
            print(f"Already organized: {file_name}")
            skipped += 1
            continue

        destination_path = destination_folder / new_name
        destination_path = get_unique_path(destination_path)

        if dry_run:
            print(f"Would move {file_name} to {category}/{destination_path.name}")
            planned += 1

        else:
            destination_folder.mkdir(parents=True, exist_ok=True)

            shutil.move(str(source_path), str(destination_path))

            print(f"Moved {file_name} to {destination_path.name}")
            moved += 1

    print("-" * 30)
    print(f"Total files moved: {moved}")
    print(f"Total files skipped: {skipped}")
    print(f"Total files planned: {planned}")
