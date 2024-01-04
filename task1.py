import shutil
from pathlib import Path
import argparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Copy and sort files.")
    parser.add_argument(
        "source",
        type=Path,
        help="Path to the source directory.",
    )
    parser.add_argument(
        "destination",
        type=Path,
        help="Path to the destination directory.",
        default=Path.cwd() / "dist",
    )
    return parser.parse_args()


def recursive_read_directory(directory: Path) -> list:
    all_files = []
    try:
        for path in directory.rglob("*"):
            if path.is_file():
                all_files.append(path)
            elif path.is_dir():
                all_files.extend(recursive_read_directory(path))
    except (PermissionError, FileNotFoundError) as e:
        print(f"Error: {e}")
    return all_files


def copy_and_sort_files(source: Path, destination: Path) -> None:
    try:
        files_to_copy = recursive_read_directory(source)
        for src_path in files_to_copy:
            extension = src_path.suffix[1:].lower()
            dest_dir = destination / extension

            dest_dir.mkdir(parents=True, exist_ok=True)

            dest_path = dest_dir / src_path.name

            shutil.copy(src_path, dest_path)
            print(f"Copied: {src_path} to {dest_path}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    args = parse_args()

    copy_and_sort_files(args.source, args.destination)
    print("Files copied and sorted successfully.")
