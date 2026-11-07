from pathlib import Path
from datetime import datetime
from organizer import get_category


def scan_folder(folder_path):
    folder_path = Path(folder_path)

    if not folder_path.exists() or not folder_path.is_dir():
        print("Invalid folder path")
        return []

    files = []
    total_size = 0

    for item in folder_path.rglob("*"):

        if not item.is_file():
            continue

        relative_path = item.relative_to(folder_path)

        file_stats = item.stat()
        size = file_stats.st_size
        modified = datetime.fromtimestamp(file_stats.st_mtime)

        file_data = {
            "name": item.name,
            "relative_path": str(relative_path),
            "extension": item.suffix.lower(),
            "size": round(size / 1024, 2),
            "modified": modified.strftime("%d-%m-%Y %H:%M:%S"),
            "category": get_category(item.suffix),
        }

        files.append(file_data)
        total_size += size

    print(f"Total files scanned: {len(files)}")
    print(f"Total size: {total_size / 1024:.2f} KB")

    for file in files:
        print("-" * 30)
        for key, value in file.items():
            print(f"{key}: {value}")

    return files
