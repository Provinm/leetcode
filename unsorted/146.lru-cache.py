#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#
# https://leetcode.com/problems/lru-cache/description/
#
# algorithms
# Hard (23.90%)
# Total Accepted:    260.7K
# Total Submissions: 1.1M
# Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
#
# 
# Design and implement a data structure for Least Recently Used (LRU) cache. It
# should support the following operations: get and put.
# 
# 
# 
# get(key) - Get the value (will always be positive) of the key if the key
# exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present.
# When the cache reached its capacity, it should invalidate the least recently
# used item before inserting a new item.
# 
# 
# Follow up:
# Could you do both operations in O(1) time complexity?
# 
# Example:
# 
# LRUCache cache = new LRUCache( 2 /* capacity */ );
# 
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4
# 
# 
#
# from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        
        self._max = capacity
        self.lru = {}

    def get(self, key: int) -> int:

        r = -1
        if key in self.lru:
            r = self.lru.get(key)
            del self.lru[key]
            self.put(key, r)
        return r

    def put(self, key: int, value: int) -> None:
        
        if key in self.lru:
            r = self.lru[key]
            del self.lru[key]
            self.put(key, r)
        else:
            if len(self.lru) >= self._max:
                del self.lru[list(self.lru)[0]]
        self.lru[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# lruc = LRUCache(2)

# lruc.put(1,1)
# lruc.put(2,2)
# lruc.get(1)
# lruc.put(3,3)
# lruc.get(2)
# lruc.put(4,4)
# lruc.get(1)
# lruc.get(3)
# lruc.get(4)

'''
√ Accepted
√ 18/18 cases passed (228 ms)
[WARN] Failed to get submission beat ratio.
'''
