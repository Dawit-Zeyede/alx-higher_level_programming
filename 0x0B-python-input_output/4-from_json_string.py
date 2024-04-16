#!/usr/bin/python3

"""Function to return a JSON object"""
import json


def from_json_string(my_str):
    """
    Return a JSON object
    """

    return json.loads(my_str)
