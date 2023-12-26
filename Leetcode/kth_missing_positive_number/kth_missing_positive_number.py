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