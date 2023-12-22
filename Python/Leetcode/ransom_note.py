"""
Given two strings ransomNote and magazine, 
return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_dict = dict()
        magazine_dict = dict()

        for char in magazine:
            if char in magazine_dict:
                magazine_dict[char] += 1
            else:
                magazine_dict[char] = 1

        for char in ransomNote:
            if char not in magazine_dict:
                return False
            else:
                if char in ransom_dict:
                    ransom_dict[char] += 1
                else:
                    ransom_dict[char] = 1
        
        for key in magazine_dict.keys():
            if key in ransom_dict:
                if magazine_dict[key] >= ransom_dict[key]:
                    pass
                else:
                    return False
        return True
