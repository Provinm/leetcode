#
# @lc app=leetcode id=126 lang=python3
#
# [126] Word Ladder II
#
# https://leetcode.com/problems/word-ladder-ii/description/
#
# algorithms
# Hard (18.39%)
# Likes:    1066
# Dislikes: 197
# Total Accepted:    129.5K
# Total Submissions: 704K
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# Given two words (beginWord and endWord), and a dictionary's word list, find
# all shortest transformation sequence(s) from beginWord to endWord, such
# that:
# 
# 
# Only one letter can be changed at a time
# Each transformed word must exist in the word list. Note that beginWord is not
# a transformed word.
# 
# 
# Note:
# 
# 
# Return an empty list if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
# 
# 
# Example 1:
# 
# 
# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
# 
# Output:
# [
# ⁠ ["hit","hot","dot","dog","cog"],
# ["hit","hot","lot","log","cog"]
# ]
# 
# 
# Example 2:
# 
# 
# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
# 
# Output: []
# 
# Explanation: The endWord "cog" is not in wordList, therefore no possible
# transformation.
# 
# 
# 
# 
# 
#

from typing import List

class LinkedList:

    def __init__(self, char):
        self.var = char
        self.next = []

    def __eq__(self, other):
        return self.var == other.var

    def __str__(self):
        return f"var = {self.var}, next = {self.next}"
    
def getlist(root, end):
    print(f'getlist node = {root}')
    if not root.next:
        # if root.var == end:
        return [root.var]
        # else:
        #     return []
    ret = []
    next_roots = root.next
    for ele in next_roots:
        sub = getlist(ele, end)
        if not sub:
            continue
        sub = [root.var] + sub
        ret.append(sub)

    return ret


beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        
        wordList = set(wordList)
        if endWord not in wordList:
            return []

        root = LinkedList(beginWord)
        point = root
        all_char = 'abcdefghijklmnopqrstuvwxyz'
        stack = [point]
        temp_stack = []
        visited = set()
        while stack:
            temp = []
            word_node = stack.pop()
            word = word_node.var
            visited.add(word)
            for idx, _ in enumerate(word):
                for supply in all_char:
                    new_char = word[:idx] + supply + word[idx+1:]
                    if new_char == endWord:
                        point.next.append(LinkedList(endWord))
                        return getlist(root, endWord)
                    elif new_char in wordList:
                        if new_char in visited:
                            continue
                        if new_char != beginWord:
                            temp.append(LinkedList(new_char))
                        
            word_node.next = temp
            temp_stack.extend(temp)
            if not stack:
                stack = temp_stack
        return []


s = Solution()
r = s.findLadders(beginWord, endWord, wordList)
print(r)

