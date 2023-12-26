from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # The purpose of using a defaultdict is to simplify the process of initializing and updating values associated with keys. 
        # With a regular dictionary (dict), if you try to access a key that doesn't exist, it raises a KeyError. 
        # However, with a defaultdict, if you access a nonexistent key, 
        # it will create that key with the default value provided by the default_factory. 
        anagram_dict = defaultdict(list)

        # Iterate over the words in the list
        for word in strs:
            # Then sort the words, because all the anagrams will be the same sorted "eat" woul become "aet"
            # aswell as tea, and that will be the key and the value the array of words
            sorted_word = "".join(sorted(word))
            anagram_dict[sorted_word].append(word)
        
        return list(anagram_dict.values())
