import csv
import itertools
from itertools import chain
from pathlib import Path
from typing import Iterable, List, Mapping, Optional, Set

import yaml


def aggregate(*args: List) -> itertools:
    return chain.from_iterable(*args)


def pairwise_combinations(names: List):
    combos = []
    for i in range(len(names) - 1):
        for j in range(i + 1, len(names)):
            combos.append([names[i], names[j]])
    return combos


def match_vals_to_keys(values: Iterable, lookup_dict: Mapping) -> Set:
    matched_keys = set()
    while values:
        element = values.pop(0)
        for person, owned_values in lookup_dict.items():
            if element in owned_values:
                matched_keys.add(person)
                break
    return matched_keys


def no_parser():
    raise KeyError(
        "File extension not supported. Supported file extensions: [yml|yaml], csv"
    )


def csv_to_dict(
    f: Path,
    name_header: Optional[str] = None,
    value_header: Optional[str] = None,
    col_delimiter: Optional[str] = None,
    val_delimiter: Optional[str] = None,
) -> Mapping:

    if not name_header:
        name_header = "Name"
    if not value_header:
        value_header = "model"
    if not col_delimiter:
        col_delimiter = ";"
    if not val_delimiter:
        val_delimiter = ","

    with open(f) as f:
        reader = csv.DictReader(f, delimiter=col_delimiter, quoting=csv.QUOTE_ALL)
        data = {
            row[name_header]: row[value_header].split(val_delimiter) for row in reader
        }
    return data


def yaml_to_dict(f: Path) -> Mapping:
    with open(f) as f:
        return yaml.safe_load(f)
