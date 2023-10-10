#!/usr/bin/python3
"""define convert to JSON from object"""

import json


def from_json_string(my_str):
    """return json string"""
    return json.loads(my_str)
