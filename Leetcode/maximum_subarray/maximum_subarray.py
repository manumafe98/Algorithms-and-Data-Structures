from typing import List

# Time complexity: O(n)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # We give the starting value as the first element of the array, because the array can have negative values
        # So its not wise to initiate this variable to 0
        max_sub_array = nums[0] 
        current_sum = 0

        # We can think about this problem similarly as a sliding window one
        # Cause we know that if the current sum is negative we can discard the numbers and point to the next one
        # [-2,1,-3,4,-1,2,1,-5,4] 
        # -2 + 1 = -1 - 3 = -4 its inconvenient to add negative values and the subarray must be contiguous
        for num in nums:
            if current_sum < 0:
                current_sum = 0
            current_sum += num
            max_sub_array = max(current_sum, max_sub_array)
        
        return max_sub_array
