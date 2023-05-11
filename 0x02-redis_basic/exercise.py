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

def call_history(method: Callable) -> Callable:
    """ store the history of inputs and outputs for a particular function """
    key = method.__qualname__
    inputs = key + ":inputs"
    outputs = key + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """ wrapped function """
        self._redis.rpush(inputs, str(args))
        data = method(self, *args, **kwds)
        self._redis.rpush(outputs, str(data))
        return data
    return wrapper

class Cache():
    """a class called cache"""

    def __init__():
        """init method of the class stores an instance of redis"""
        self.redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
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

def replay(method: Callable):
    """ display the history of calls of a particular function """
    key = method.__qualname__
    inputs = key + ":inputs"
    outputs = key + ":outputs"
    redis = method.__self__._redis
    count = redis.get(key).decode("utf-8")
    print("{} was called {} times:".format(key, count))
    inputList = redis.lrange(inputs, 0, -1)
    outputList = redis.lrange(outputs, 0, -1)
    redis_zipped = list(zip(inputList, outputList))
    for a, b in redis_zipped:
        attr, data = a.decode("utf-8"), b.decode("utf-8")
        print("{}(*{}) -> {}".format(key, attr, data))
