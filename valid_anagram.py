# Leetcode
"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            s_dict = dict()
            t_dict = dict()
            # With the first loop we create the dictionaries with the keys being the chars of the word
            # And the values the times they appear in the word for example "anagram" {"a": 2}
            for i in range(len(s)):
                if s[i] in s_dict:
                    s_dict[s[i]] += 1
                else:
                    s_dict[s[i]] = 1
                
                if t[i] in t_dict:
                    t_dict[t[i]] += 1
                else:
                    t_dict[t[i]] = 1
            
            # Then we loop the keys of one of the dict and check if they are in the other one 
            # and compare the times they appear
            for key in s_dict.keys():
                if key in t_dict and s_dict[key] == t_dict[key]:
                    continue
                else:
                    return False
            return True
        else:
            return False
