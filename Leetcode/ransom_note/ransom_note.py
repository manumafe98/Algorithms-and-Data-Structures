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
