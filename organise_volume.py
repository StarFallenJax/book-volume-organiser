#!/usr/bin/env python3
from __future__ import annotations

# argparse is used to read command line arguments
# shutil is used to copy files
# pathlib is used for path handling across mac windows and linux
import argparse
import shutil
from pathlib import Path


def organise_volume(input_dir: Path, output_dir: Path) -> None:
    # make sure the input path exists and is a folder
    if not input_dir.exists() or not input_dir.is_dir():
        raise SystemExit(f"error: input folder does not exist or is not a folder: {input_dir}")

    # create the output folder if it does not already exist
    output_dir.mkdir(parents=True, exist_ok=True)

    # total_i counts every file copied across all chapters
    total_i = 1

    # chapter counts which subfolder is currently processing
    chapter = 1

    # collect all subfolders inside the input directory
    # only folders are treated as chapters
    subfolders = [p for p in input_dir.iterdir() if p.is_dir()]

    # sort subfolders by name to keep chapter order consistent
    subfolders.sort(key=lambda p: p.name.lower())

    # loop through each chapter folder
    for sub in subfolders:
        # chapter_i counts files inside the current chapter
        chapter_i = 1

        # collect all files inside the chapter folder
        # filenames like 01 02 etc are ignored for naming
        files = [p for p in sub.iterdir() if p.is_file()]

        # sort files so numbered images copy in order
        files.sort(key=lambda p: p.name.lower())

        # loop through each file in the chapter
        for f in files:
            # build the new filename using counters only
            # original name is ignored except for extension
            new_name = f"Ch{chapter}-{chapter_i} ({total_i}){f.suffix}"

            # destination path inside the output folder
            dest = output_dir / new_name

            # copy the file to the new location
            # copy2 preserves timestamps and metadata
            shutil.copy2(f, dest)

            # increment per chapter counter
            chapter_i += 1

            # increment global counter
            total_i += 1

        # move to next chapter after finishing folder
        chapter += 1


def main() -> None:
    # set up command line argument parsing
    parser = argparse.ArgumentParser(
        description="copy files from subfolders into one organised volume folder with renamed numbering"
    )

    parser.add_argument("folder", help="folder that contains chapter subfolders")

    # optional output folder argument
    # defaults to a folder named organised volume
    parser.add_argument(
        "-o",
        "--output",
        default="Organised Volume",
        help="output folder name or path",
    )

    args = parser.parse_args()

    # convert input and output to absolute resolved paths
    organise_volume(
        Path(args.folder).expanduser().resolve(),
        Path(args.output).expanduser().resolve()
    )


if __name__ == "__main__":
    main()
