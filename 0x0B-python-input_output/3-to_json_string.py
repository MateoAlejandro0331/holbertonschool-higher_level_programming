#!/usr/bin/python3
import json
"""
    Funtion that returns the JSON representation
"""


def to_json_string(my_obj):
    represent = json.dumps(my_obj)
    return represent
