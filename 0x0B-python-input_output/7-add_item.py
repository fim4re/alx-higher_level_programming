#!/usr/bin/python3
"""Python list arg and save them to a file."""
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    items_data = load_from_json_file("add_item.json")
except Exception:
    items_data = []

items_data.extend(sys.argv[1:])
save_to_json_file(items_data, "add_item.json")
