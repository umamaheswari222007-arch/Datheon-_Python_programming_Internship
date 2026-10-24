
import os
import shutil
from pathlib import Path

# Downloads folder
DOWNLOADS_FOLDER = Path.home() / "Downloads"

# File extension mapping
EXTENSION_MAPPING = {
    # Documents
    ".pdf": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".xls": "Documents",
    ".xlsx": "Documents",
    ".ppt": "Documents",
    ".pptx": "Documents",

    # Images
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".bmp": "Images",

    # Videos
    ".mp4": "Videos",
    ".mkv": "Videos",
    ".avi": "Videos",
    ".mov": "Videos",

    # Audio
    ".mp3": "Audio",
    ".wav": "Audio",
    ".aac": "Audio",

    # Archives
    ".zip": "Archives",
    ".rar": "Archives",
    ".7z": "Archives",
    ".tar": "Archives",

    # Code files
    ".py": "Code",
    ".html": "Code",
    ".css": "Code",
    ".js": "Code",
    ".java": "Code",
    ".cpp": "Code"
}


def get_category(file_path):
    """Return the category based on the file extension."""
    extension = file_path.suffix.lower()
    return EXTENSION_MAPPING.get(extension, "Others")


def get_unique_path(destination):
    """Generate a unique filename if it already exists."""
    if not destination.exists():
        return destination

    counter = 1

    while True:
        new_destination = destination.with_name(
            f"{destination.stem}_{counter}{destination.suffix}"
        )

        if not new_destination.exists():
            return new_destination

        counter += 1


def organize_files(folder_path):
    """Organize files into category folders."""

    moved_count = 0
    skipped_count = 0
    error_count = 0

    print("\n" + "=" * 50)
    print("       AUTOMATIC FILE ORGANIZER")
    print("=" * 50)

    try:
        folder_path = Path(folder_path)

        if not folder_path.is_dir():
            print("Error: The selected folder does not exist.")
            return

        with os.scandir(folder_path) as entries:
            for entry in entries:

                # Skip directories
                if not entry.is_file():
                    continue

                source = Path(entry.path)

                try:
                    # Identify file category
                    category = get_category(source)

                    # Create category folder
                    destination_folder = folder_path / category
                    destination_folder.mkdir(
                        parents=True,
                        exist_ok=True
                    )

                    # Generate destination path
                    destination = get_unique_path(
                        destination_folder / source.name
                    )

                    # Move the file
                    shutil.move(str(source), str(destination))

                    print(
                        f"Moved: {source.name} -> "
                        f"{category}/{destination.name}"
                    )

                    moved_count += 1

                except PermissionError:
                    print(f"Permission denied: {source.name}")
                    skipped_count += 1

                except OSError as error:
                    print(f"Error moving {source.name}: {error}")
                    error_count += 1

    except PermissionError:
        print("Permission denied while accessing the folder.")

    except OSError as error:
        print(f"Error accessing the folder: {error}")

    # Execution summary
    print("\n" + "=" * 50)
    print("          EXECUTION SUMMARY")
    print("=" * 50)
    print(f"Files relocated : {moved_count}")
    print(f"Files skipped   : {skipped_count}")
    print(f"Errors          : {error_count}")
    print("=" * 50)


# Main program
if __name__ == "__main__":
    organize_files(DOWNLOADS_FOLDER)
