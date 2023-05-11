#!/usr/bin/env python3
import redis, uuid

class Cache():

    def __init__():
        _redis = redis.Redis()
        _redis.flushdb

    def store(data) -> str:
        key = uuid.uuid4()
        _redis.set({key: data})
        return key
