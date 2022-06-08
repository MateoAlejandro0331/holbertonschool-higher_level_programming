#!/usr/bin/python3
"""Import module"""
import json
"""
    Funtion that returns the JSON representation
"""


def to_json_string(my_obj):
    """My Funtion"""
    represent = json.dumps(my_obj)
    return represent
