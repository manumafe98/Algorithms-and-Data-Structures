"""
Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written. 
Do the above modifications to the input array in place and do not return anything.

 

Example 1:

Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
Example 2:

Input: arr = [1,2,3]
Output: [1,2,3]
Explanation: After calling your function, the input array is modified to: [1,2,3]
 

Constraints:

1 <= arr.length <= 104
0 <= arr[i] <= 9
"""
from typing import List

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        # Create a pointer and a empty array
        pointer = 0
        temp_array = []

        # loop over the length of the array
        while pointer < len(arr):
            # if its 0 add another 0
            if arr[pointer] == 0:
                temp_array.append(0)

            temp_array.append(arr[pointer])
            pointer += 1
        
        # cut the array on the length of arr
        temp_array = temp_array[0:len(arr)]
        # copy temp to arr
        arr[:] = temp_array
