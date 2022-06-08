#!/usr/bin/python3
"""import module"""
import json
"""
    function that creates an Object from a “JSON file”:
"""


def load_from_json_file(filename):
    """My function"""
    with open(filename, 'r', encoding='utf-8') as file:
        obj = json.load(file)
        return obj
