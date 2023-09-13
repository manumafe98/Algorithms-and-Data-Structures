# Leetcode
"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
find two numbers such that they add up to a specific target number. 
Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

 

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
 

Constraints:

2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.
"""
from typing import List

# My solution
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = []
        for idx, val in enumerate(numbers):
            if len(result) == 2:
                break
            temp = target - val
            if temp == val:
                result.append(idx + 1)
            else:
                if temp in numbers:
                    result.append(idx + 1)
                    result.append(numbers.index(temp) + 1)
                    break
        return result

# Two pointers solution
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Create two pointers where one points at the first index in the array and the other points at the second index.
        p1, p2 = 0, 1;
        while not numbers[p1] + numbers[p2] == target:
            # If the sum of the values at the pointers is less than the target, shift both pointers over one.
            if numbers[p1] + numbers[p2] < target:
                p2+=1;
                p1+=1;
            # If the values summed are greater, shift the first pointer left one.
            else:
                p1-=1; 
        return [p1+1, p2+1]
