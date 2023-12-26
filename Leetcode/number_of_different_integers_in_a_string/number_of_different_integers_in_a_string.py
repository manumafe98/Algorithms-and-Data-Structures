class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        digit_dict = dict()

        for char in word:
            if char.isdigit():
                pass
            else:
                word = word.replace(char, " ")
        
        digit_array = word.split(" ")
        for num in digit_array:
            if num.isdigit():
                digit_dict[int(num)] = True
        
        return len(list(digit_dict))
