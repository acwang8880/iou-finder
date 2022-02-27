# cd ..
# export PYTHONPATH="."
from collections import OrderedDict

import iou.find_combinations
import iou.helpers


def test_aggregate1():
    args = [[1, 2, 3, 4, 5], [1, 2, 3, 5], [2, 4, 6]]
    expected = [1, 2, 3, 4, 5, 1, 2, 3, 5, 2, 4, 6]
    actual = list(iou.helpers.aggregate(args))
    assert expected == actual


def test_aggregate2():
    args = [[9, 8, 7], [1, 2, 3, 4], [1], []]
    expected = [9, 8, 7, 1, 2, 3, 4, 1]
    actual = list(iou.helpers.aggregate(args))
    assert expected == actual


def test_pairwise_combinations1():
    args = [0, 1, 2, 3, 4]
    expected = [
        [0, 1],
        [0, 2],
        [0, 3],
        [0, 4],
        [1, 2],
        [1, 3],
        [1, 4],
        [2, 3],
        [2, 4],
        [3, 4],
    ]
    actual = iou.helpers.pairwise_combinations(args)
    assert expected == actual


def test_pairwise_combinations2():
    args = OrderedDict({"d": 100, "c": 99, "b": 77, "a": 1})
    expected = [
        ["d", "c"],
        ["d", "b"],
        ["d", "a"],
        ["c", "b"],
        ["c", "a"],
        ["b", "a"],
    ]
    actual = iou.helpers.pairwise_combinations(list(args.keys()))
    assert expected == actual


def test_match_values1():
    lookup_dict = OrderedDict(
        {
            "alex": [1, 2, 3, 5],
            "meimei": [6, 7, 4],
            "webb": [1, 3],
            "pei": [6, 7],
            "kelvin": [4, 8],
        }
    )
    print(lookup_dict)
    expected = {"alex", "meimei", "kelvin"}
    args = [2, 5, 1, 3, 6, 7, 4, 8]
    actual = iou.helpers.match_vals_to_keys(args, lookup_dict)
    assert expected == actual


def test_read_file_csv1():
    file = "files/testfile.csv"
    expected = {
        "meimei": ["6", "7", "4"],
        "alex": ["1", "2", "3", "5"],
        "webb": ["1", "3"],
        "pei": ["6", "7"],
        "kelvin": ["4", "8"],
    }
    actual = iou.find_combinations.read_file(file, "Name", "model")
    print(actual)
    assert expected == actual

print(__file__)
