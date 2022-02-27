from pathlib import Path
from typing import Optional

import argh

import iou.find_combinations


@argh.arg(
    "filepath", help="Path to a file containing a map of ids to a list of their values."
)
@argh.arg("--name_header", help="Key of the name column", default="Name")
@argh.arg("--value_header", help="Key of the models column", default="model")
@argh.arg("--col_delim", help="Delimiter to split columns", default=";")
@argh.arg("--val_delim", help="Delimiter to split values", default=",")
def find_combos(
    filepath: str,
    name_header: Optional[str] = None,
    value_header: Optional[str] = None,
    col_delim: Optional[str] = None,
    val_delim: Optional[str] = None,
):
    """Find the combination of people that completes all of the models."""
    target_file = Path(filepath)
    if not target_file.is_file():
        print(f"Your path does not point to a valid file: {filepath}")
        raise FileNotFoundError

    data = iou.find_combinations.read_file(
        target_file,
        name_header=name_header,
        value_header=value_header,
        col_delimiter=col_delim,
        val_delimiter=val_delim,
    )
    print(data)

    print(iou.find_combinations.compute(data))


def main():
    argh.dispatch_commands([find_combos])


if __name__ == "__main__":
    main()
