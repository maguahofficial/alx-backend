#!/usr/bin/python3
"""  The Basic dictionary """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ The class that inherits from BaseCaching and is a caching system
        caching system doesn't have limit """
    def put(self, key, item):
        """ Function assigns to the dictionary """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Function return the value linked """
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key)
