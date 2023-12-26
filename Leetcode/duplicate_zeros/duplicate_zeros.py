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
