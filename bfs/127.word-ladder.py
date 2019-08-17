#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#
# https://leetcode.com/problems/word-ladder/description/
#
# algorithms
# Medium (24.59%)
# Likes:    1544
# Dislikes: 829
# Total Accepted:    272.4K
# Total Submissions: 1.1M
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# Given two words (beginWord and endWord), and a dictionary's word list, find
# the length of shortest transformation sequence from beginWord to endWord,
# such that:
# 
# 
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that beginWord is not
# a transformed word.
# 
# 
# Note:
# 
# 
# Return 0 if there is no such transformation sequence.
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
# Output: 5
# 
# Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" ->
# "dog" -> "cog",
# return its length 5.
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
# Output: 0
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

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        all_char = 'abcdefghijklmnopqrstuvwxyz'
        
        stack = [beginWord]
        ret = 1
        temp = []
        while stack:
            word = stack.pop()
            for idx, _ in enumerate(word):
                for supply in all_char:
                    new_char = word[:idx] + supply + word[idx+1:]
                    if new_char == endWord:
                        return ret+1
                    elif new_char in wordList:
                        if new_char != beginWord:
                            temp.append(new_char)
                        wordList.remove(new_char)
            if not stack:
                ret += 1
                stack = temp
                temp = []
        return 0

'''
√ Accepted
  √ 40/40 cases passed (484 ms)
  √ Your runtime beats 29.68 % of python3 submissions
  √ Your memory usage beats 48.28 % of python3 submissions (14.6 MB)

'''
