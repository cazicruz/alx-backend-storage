#!/usr/bin/env python3
import redis, uuid


class Cache():
    """a class called cache"""

    def __init__():
        """init method of the class stores an instance of redis"""
        self.redis = redis.Redis()
        self._redis.flushdb

    def store(data) -> str:
        """stores data in Redis using the a random value
        as key and returns the key"""
        key = uuid.uuid4()
        self._redis.set({str(key): data})
        return key
