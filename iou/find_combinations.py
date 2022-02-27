#!/usr/bin/python3

from collections import OrderedDict
from pathlib import Path
from typing import Mapping, Optional, Set

from iou.helpers import (aggregate, csv_to_dict, match_vals_to_keys, no_parser,
                         pairwise_combinations, yaml_to_dict)


def compute(people: Mapping) -> Set:
    sorted_people = OrderedDict(
        {
            key: people[key]
            for key in sorted(people, key=lambda key: len(people[key]), reverse=True)
        }
    )

    total = list(aggregate(values for values in sorted_people.values()))

    # trim your total list
    for pair in pairwise_combinations(list(sorted_people.keys())):
        element_set_to_remove = set.intersection(
            *[set(sorted_people[person]) for person in pair]
        )
        for val in element_set_to_remove:
            total.remove(val)

    # match models to people
    return match_vals_to_keys(total, sorted_people)


def read_file(
    path: str,
    name_header: Optional[str] = None,
    value_header: Optional[str] = None,
    col_delimiter: Optional[str] = None,
    val_delimiter: Optional[str] = None,
) -> Mapping:

    # suffix_to_parser = {
    #     ".yml": yaml.safe_load,
    #     ".yaml": yaml.safe_load,
    #     ".csv": csv_to_dict,
    #     # ".json": json.load
    #     None: no_parser,
    # }

    path = Path(path)

    if path.suffix in (".yml", ".yaml"):
        return yaml_to_dict(path)
    elif path.suffix == ".csv":
        return csv_to_dict(
            path, name_header, value_header, col_delimiter, val_delimiter
        )
    else:
        return no_parser()
