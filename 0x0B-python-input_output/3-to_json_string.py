#!/usr/bin/python3
"""define convert to JSON"""

import json


def to_json_string(my_obj):
    """return json format of an object"""
    return json.dumps(my_obj)
