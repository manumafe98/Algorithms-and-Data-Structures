from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # We apply binary search
        n = len(nums)

        start = 0
        end = n - 1

        while start <= end:
            # Calculate the middle
            mid = (end + start) // 2
            
            if nums[mid] == target:
                return mid
            
            if nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        # If the loop ends without returning we return the start value
        # Because it would represent the position to insert the value
        return start

"""
Examples:
-------------
nums = [2] 
target = 1
The start and end pointer would be at index 0
And as the target is smaller we shift the end pointer to the left
But as that does not make sense, and the loop would end we return the start index
Remaining the array [1, 2]

-------------
nums = [2]
target = 3
In this case as the target is bigger we shift the start value to the right
So as start > end the loop would end and start would be index + 1
Remaining the aray [2, 3]

"""