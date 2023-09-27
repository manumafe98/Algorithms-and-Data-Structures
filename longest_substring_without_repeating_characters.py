# Leetcode
"""
Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""
# Time complexity: O(N)
# Sliding window technique applied
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # We use a set, because consumes less memory than a dict and does not allow duplicates
        # Also the "in" method is O(1) in sets
        char_set = set()
        # Define a left pointer
        l = 0
        res = 0

        # Then our right pointer is going to be updated when looping over the characters
        for r in range(len(s)):
            # If the next character to add to the set is already in it, we loop over the set and remove
            # the left characters until there are no duplicates, and then add the char
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            # Calculate the max between the size of the set and the current res
            res = max(res, len(char_set))
        return res
