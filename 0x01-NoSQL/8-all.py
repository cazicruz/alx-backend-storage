#!/usr/bin/env python3
""" a Python function that lists all documents in a collection"""


def list_all(mongo_collection):
    """if mongo_collection empty return an empty list"""
    return(mongo_collection.find())
