from typing import List

class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        # Define two variables, current maximum subarray and longest
        longest = 0 
        current = 0 
        for i in range(len(nums)):
            # First check if the number meets the threshold criteria
            if nums[i] > threshold: 
                current = 0 
            # Then if the subarray wasn't initialized, check for a even number
            elif current == 0 and nums[i] % 2 == 0: 
                current = 1 
            # If the subarray was started check if the previous value meet the condition nums[i] % 2 != nums[i - 1] % 2
            # For simplicity instead of checking the next one check the previous one
            elif current > 0 and nums[i] % 2 != nums[i - 1] % 2: 
                current += 1 
            # 
            else: 
                # A good example to undestand this else is for example nums = [2, 2, 3] threshold = 4
                # With the first 2, current = 1, the 2dn 2 will not met the criteria, but can start a new valid 
                # subarray, thats why it checks if its even, and set it to 1 and if not 0
                current = 1 if nums[i] % 2 == 0 else 0
            
            # Get the maximum between longest and current, every iteration
            # For cases like [2, 8] so longest will store 1 and then fail with 8, but return 1
            longest = max(longest, current) 
        return longest
