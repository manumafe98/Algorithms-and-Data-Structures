from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create the dict of the frequency the numbers appear
        frequency_dict = dict()
        for num in nums:
            if num in frequency_dict:
                frequency_dict[num] += 1
            else:
                frequency_dict[num] = 1

        result = []
        # Loop K times
        for _ in range(0, k):
            # Get the current maximum value and hold the key in the variable
            max_key = max(frequency_dict, key=frequency_dict.get)
            # Append the key to the result array
            result.append(max_key)
            # And then pop the key from the dict
            frequency_dict.pop(max_key)
        
        return result
