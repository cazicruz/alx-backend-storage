#!/usr/bin/env python3
from typing import Union, Callable, Optional, Any
import redis, uuid


class Cache():
    """a class called cache"""

    def __init__():
        """init method of the class stores an instance of redis"""
        self.redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """stores data in Redis using the a random value
        as key and returns the key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
