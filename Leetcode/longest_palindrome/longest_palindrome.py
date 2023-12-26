class Solution:
    def longestPalindrome(self, s: str) -> int:
        # We define a dict
        char_count_dict = dict()

        # Then two variables, to hold the total and biggest odd number
        total = 0
        greatest_odd_number = 0

        # We create the dictionary to hold the chars with the amount of times they appear
        for char in s:
            if char in char_count_dict:
                char_count_dict[char] += 1
            else:
                char_count_dict[char] = 1
        
        # Then we iterate over the keys of that dict
        for key in char_count_dict.keys():

            # if its a even number add it to total
            if char_count_dict[key] % 2 == 0:
                total += char_count_dict[key]
            
            # if not hold it in greatest_odd_number
            else:
                if char_count_dict[key] > greatest_odd_number:

                    # if there was a value in greatest_odd_number like 3/5 you can use 2 or 4 chars 
                    # of them to make a palindrome so add to the total that number -1 and then set the new biggest one
                    if greatest_odd_number - 1 != 0 and (greatest_odd_number - 1) % 2 == 0:
                        total += (greatest_odd_number - 1)
                    greatest_odd_number = char_count_dict[key]
                # And if there is a odd numer that is not greater than the current greatest_odd_number
                # Do the same check - 1
                else:
                    if char_count_dict[key] - 1 != 0 and (char_count_dict[key] - 1) % 2 == 0:
                        total += (char_count_dict[key] - 1)
        return total + greatest_odd_number
