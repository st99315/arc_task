#!/usr/bin/env python

"""Read and Write for JSON file."""

from __future__ import print_function
import json


def read_json(path):
    """Read a JSON file from path, and convert to object of python."""
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
    """Write object of python to specify JSON file using JSON format."""
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
    """Print content and specify category for desired."""
    for each in content[category]:
        print(each)

def _test():
    """Testing function and demonstration."""
    file_path = "./example_pick_task/item_location_file.json"
    content = read_json(file_path)
    print_element(content, "bins")
    print_element(content, "boxes")
    print_element(content, "tote")

    new_path = "./test.json"
    write_json(new_path, content)

if __name__ == "__main__":
    _test()

    # object of python for json format.
    # content = {"test": [
    #     {"size_id": "123", "contents": ["mac", "apple"]},
    #     {"size_id": "887", "contents": ["box", "pencil", "pen"]},
    #     {"size_id": "553", "contents": ["maxos", "watch"]}
    # ]}
