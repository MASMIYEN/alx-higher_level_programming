#!/usr/bin/python3
""" create object from a JSON file"""
import json


def load_from_json_file(filename):
    """create object from JSON  file"""
    with open(filename, 'r', encoding="utf-8") as file:
        return json.load(file)
