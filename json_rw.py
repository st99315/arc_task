#!/usr/bin/env python

"""JSON file test."""

from __future__ import print_function
import json


def read_json(path):
    """Read a JSON file from path, and convet to python object."""
    try:
        with open(path) as f:
            content = json.load(f)
            # or following
            # content = json.loads(f.read())
            return content
    except IOError as e:
        print(e)
        return None

def write_json(path, content):
    """Write object of python to spec JSON file using JSON format."""
    try:
        with open(path, 'w') as f:
            json.dump(content, f, indent=4, separators=(',', ': ')) # sort_keys=True
            # or following, assume content is str obj
            # f.write(json.dumps(content, f, indent=4, separators=(',', ': ')))
        return True
    except IOError as e:
        print(e)
        return False

def print_element(content, category):
    """Print content and spec category for desired."""
    for each in content[category]:
        print(each)


if __name__ == "__main__":

    file_path = "./example_pick_task/item_location_file.json"
    content = read_json(file_path)
    print_element(content, "bins")
    print_element(content, "boxes")
    print_element(content, "tote")

    new_path = "./test.json"


    # content = {"test": [
    #     {"size_id": "123", "contents": ["mac", "apple"]},
    #     {"size_id": "887", "contents": ["box", "pencil", "pen"]},
    #     {"size_id": "553", "contents": ["maxos", "watch"]}
    # ]}

    write_json(new_path, content)
