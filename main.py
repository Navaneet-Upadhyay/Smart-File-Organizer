from file_scanner import scan_folder
from organizer import organize_files


def main():
    folder_path = input("Enter folder path to organize: ")

    files = scan_folder(folder_path)

    if not files:
        print("No files found.")
        return

    print("\nPreview of planned changes:")
    organize_files(files, folder_path, dry_run=True)

    choice = input("\nProceed with organizing? (yes/no): ").strip().lower()

    if choice in ("yes","y"):
        organize_files(files, folder_path, dry_run=False)
    else:
        print("Organization cancelled.")


if __name__ == "__main__":
    main()
