# Leetcode
"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
"""
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