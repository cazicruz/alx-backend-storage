#!/usr/bin/env python3
"""a Python function that returns the list of
school having a specific topic:"""
from typing import List

def schools_by_topic(mongo_collection, topic) -> List:
    """
    mongo_collection : pymongo obj
    topic : string
    """
    return mongo_collection.find({"topics": topic})
