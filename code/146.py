# Solution 1 Failed
# Solution 1 176ms
from collections import OrderedDict
class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = OrderedDict()
        self.cap = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        ret = self.cache.pop(key)
        self.cache[key] = ret
        return ret


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.cache:
            self.cache.pop(key)
        else:
            if self.cap > 0:
                self.cap -= 1
            else:
                self.cache.popitem(last=False)
        self.cache[key] = value


# Your LRUCache object will be instantiated and called as such:
cache = LRUCache(2)

cache.get(2)
cache.put(2,6)
cache.get(1)
print(cache.cache)
cache.put(1,5)
print(cache.cache)
cache.put(1,2)
print(cache.cache)
cache.get(1)
print(cache.cache)
cache.get(2)
print(cache.cache)