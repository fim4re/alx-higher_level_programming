#!/usr/bin/python3
"""Python list arg and save them to a file."""
import sys


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
__import__('6-load_from_json_file').load_from_json_file

    arg = list(sys.argv[1:])

    try:
        items_data = load_from_json_file("add_item.json")
    except Exception:
        items_data = []
        items_data.extend(arg)
        save_to_json_file(items_data, "add_item.json")
