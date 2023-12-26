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
