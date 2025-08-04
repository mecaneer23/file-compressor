#!/usr/bin/env python3
"""
Compress a txt file using a custom algorithm.
"""

from argparse import ArgumentParser, Namespace
from pathlib import Path


class TypedNamespace(Namespace):
    """Custom Namespace class to handle typed arguments."""

    input_file: Path
    output_file: Path


def get_args() -> TypedNamespace:
    """Parse command line arguments for the script."""
    parser = ArgumentParser(
        description="Compress a text file using a custom algorithm.",
    )
    parser.add_argument(
        "input_file",
        type=Path,
        help="Path to the input text file to compress.",
    )
    parser.add_argument(
        "output_file",
        type=Path,
        nargs="?",
        default=None,
        help="Path to save the compressed output file.",
    )

    args = parser.parse_args(namespace=TypedNamespace())
    if not args.output_file:
        args.output_file = Path(args.input_file).with_suffix(".compressed")
    return args


def prompt(message: str) -> bool:
    """Prompt the user for confirmation."""
    response = input(f"{message} (y/n): ").strip().lower()
    return response == "y"


def compress_data(data: str) -> str:
    """Custom compression algorithm"""
    print("Compressing data... (not implemented)")
    return data


def main() -> str:
    """Main function to handle file compression."""
    args = get_args()

    if not args.input_file.exists():
        return f"Error: The input file '{args.input_file}' does not exist."

    with args.input_file.open("r") as infile:
        data = infile.read()

    if (
        args.output_file.exists()
        and args.output_file.stat().st_size > 0
        and not prompt(
            f"The output file '{args.output_file}' is not empty. Continue?",
        )
    ):
        return "Compression aborted due to existing output file."

    compressed_data = compress_data(data)

    with args.output_file.open("w", encoding="utf-8") as outfile:
        outfile.write(compressed_data)

    return (
        f"File '{args.input_file}' compressed "
        f"successfully to '{args.output_file}'."
    )


if __name__ == "__main__":
    print(main())  # noqa: T201
