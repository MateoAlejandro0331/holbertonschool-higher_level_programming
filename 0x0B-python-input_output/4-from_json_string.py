#!/usr/bin/python3
import json
"""
    Funtion that returns an object (Python data structure)
    represented by a JSON string
"""


def from_json_string(my_str):
    """My Funtion to returns representation"""
    represent = json.loads(my_str)
    return represent
