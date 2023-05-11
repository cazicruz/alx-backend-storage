#!/usr/bin/env python3
from typing import Union, Optional, Callable
from functools import wraps
import redis, uuid


def count_call(called_func: Callable) -> Callable:
    """a function to count the times a callable is called"""
    key = called_func.__qualname__

    @wraps(called_func):
    def wrapper(self, *args, **kwargs):
        """ wrapper function"""
        self._redis.incr(key)
        return called_func(self, *args, **kwds)
    return wrapper

@count_calls
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

    def get(self, key: str, fn: Optional[Callable] = None):
        key_value =self._redis.get(key)
        if fn:
            return fn(key_value)
        return key_value

    def get_str(self, key_value: str) ->:
        return key_value.decode("utf-8")

    def get_int(self, key_value: str) ->:
        try:
            key_value = int(value.decode("utf-8"))
        except Exception:
            key_value = 0
        return key_value
