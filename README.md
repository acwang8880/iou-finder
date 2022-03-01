# Intersection Finder

Not actually using iou

## Installation

```console
❯ source <your_venv>/bin/activate

❯ git clone https://github.com/acwang8880/iou-finder.git

❯ cd iou-finder

❯ pip install poetry

❯ poetry install

❯ iou find-combos -h
usage: iou find-combos [-h] [--name_header NAME_HEADER]
                       [--value_header VALUE_HEADER] [--col_delim COL_DELIM]
                       [--val_delim VAL_DELIM]
                       filepath

Find the combination of people that completes all of the models.

positional arguments:
  filepath              Path to a file containing a map of ids to a list of
                        their values.

optional arguments:
  -h, --help            show this help message and exit
  --name_header NAME_HEADER
                        Key of the name column (default: 'Name')
  --value_header VALUE_HEADER
                        Key of the models column (default: 'model')
  --col_delim COL_DELIM
                        Delimiter to split columns (default: ';')
  --val_delim VAL_DELIM
                        Delimiter to split values (default: ',')
```
