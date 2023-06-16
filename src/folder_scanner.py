# import argparse
from argparse import ArgumentError, Namespace
import argparse
import logging
from pathlib import Path
import shutil
from typing import List


class MySpace(Namespace):
    path: Path
    extensions: List[str]
    output: Path


def parse_path_argument(
    check_existence=True,
    check_file=False,
    check_folder=False,
    create_folder_if_doesnt_exist=False,
    create_file_if_doesnt_exist=False,
):
    check_existence = (
        check_existence
        if check_existence
        else create_file_if_doesnt_exist or create_folder_if_doesnt_exist
    )

    def _inner(path_arg: str) -> Path:
        path = Path(path_arg)
        if check_existence and not path.exists():
            if create_folder_if_doesnt_exist:
                path.mkdir()
            elif create_file_if_doesnt_exist:
                path.touch()
            else:
                raise FileNotFoundError(f"Provided path doesn't exist: {str(path)}")
        if check_folder and not path.is_dir():
            raise ArgumentError(f"Provided path is not a directory: {str(path)}")
        if check_file and not path.is_file():
            raise ArgumentError(f"Provided path is not a file: {str(path)}")

        return path

    return _inner


def get_arguments() -> MySpace:
    parser = argparse.ArgumentParser("Folder scanner tools")
    MySpace.path = parser.add_argument(
        "path",
        type=parse_path_argument(check_existence=True, check_folder=True),
        help="Folder path to perform file scan on",
    )
    MySpace.extensions = parser.add_argument(
        "--extensions",
        nargs="+",
        default=[".jpg"],
        help="File extensions to search for.",
    )
    MySpace.output = parser.add_argument(
        "--output",
        type=parse_path_argument(
            check_existence=True,
            create_folder_if_doesnt_exist=True,
        ),
        default=Path("."),
        help="Output directory",
    )

    return parser.parse_args()


def main():
    args = get_arguments()
    path = args.path
    extensions = args.extensions

    files = [file for file in path.rglob("*") if file.suffix in extensions]
    print(files)
    for file in files:
        destination = args.output / file.name
        index = 0
        while destination.exists():
            new_file_name = file.stem + "." + str(index) + file.suffix
            destination = args.output / new_file_name
            index += 1
        shutil.copyfile(file, destination)
    logging.info("Successful file copy.")


if __name__ == "__main__":
    main()
