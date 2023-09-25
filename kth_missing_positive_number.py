# Leetcode
"""
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Return the kth positive integer that is missing from this array.

 

Example 1:

Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
Example 2:

Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.
 

Constraints:

1 <= arr.length <= 1000
1 <= arr[i] <= 1000
1 <= k <= 1000
arr[i] < arr[j] for 1 <= i < j <= arr.length
"""
from typing import List

# Time complexity O(N)
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing_nums_array = []
        i = 1
        j = 0

        while j < k:
            if i in arr:
                pass
            else:
                missing_nums_array.append(i)
                j += 1
            i += 1
        
        return missing_nums_array[j - 1]

# Time complexity O(log(n))
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        start = 0
        end = len(arr) - 1

        while start <= end:
            mid = (start + end) // 2
            # This formula is to calculate how many missings are until that number
            # We know for example arr = [2,3,4,7,11] that number 7 normally if no numbers are missing
            # must be in position 6, cause indexes start from 0, so thats why number - index - 1 is the formula
            miss = arr[mid] - mid - 1

            # Then we check if there are more or less missings that we expect in that portion of the array
            if k > miss:
                start = mid + 1
            else:
                end = mid - 1
        
        # Then we return k + end + 1
        return k + end + 1