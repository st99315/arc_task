#!/usr/bin/env python

"""Get location of item in which bin and place into which box."""
"""for picking challenage."""

from __future__ import print_function
from os import path
from json_rw import read_json


class PickInfo:
    """Storage information of picking task."""

    def __init__(self, item="", form_bin="", to_box=""):
        """Init object for information of picking task."""
        self.item = item
        self.from_bin = form_bin
        self.to_box = to_box


def make_picking_list(item_loc_path, order_path):
    """Using item location file and order file to make a list for picking task."""
    item_loc_json = read_json(item_loc_path)
    order_json = read_json(order_path)

    pick_list = list()
    for order in order_json["orders"]:
        box_id = order["size_id"]
        for item in order["contents"]:
            bin_id = search_item(item_loc_json, item)
            if bin_id is not None:
                pick_list.append(PickInfo(item, bin_id, box_id))
    return pick_list

def search_item(item_loc_json, target):
    """Searching target item in which bin."""
    for bin in item_loc_json["bins"]:
        for item in bin["contents"]:
            if item == target:
                return bin["bin_id"]
    return None

def _test():
    """Testing function."""
    direcotry = "./example_pick_task"
    ilf = "item_location_file.json"
    orf = "order_file.json"

    item_loc_path = path.join(direcotry, ilf)
    order_path = path.join(direcotry, orf)

    pick_list = make_picking_list(item_loc_path, order_path)
    for info in pick_list:
        print("item:", info.item, "from_bin:", info.from_bin, "to_box:", info.to_box)
    

if __name__ == "__main__":
    _test()
