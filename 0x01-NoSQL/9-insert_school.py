#!/usr/bin/env python3
""" a Python function that inserts a new document
in a collection based on kwargs"""


def insert_school(mongo_collection, **kwargs):
    """returns the new id of the entry"""
    collection = mongo_collection.insert_one(kwargs)
    return collection.inserted_id
