from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        start = 0
        end = n - 1

        # Test the target agains the last element of the  array
        if target >= letters[-1]:
            return letters[0]

        # Then apply binary search
        while start <= end:
            mid = (start + end) // 2

            if letters[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        
        # And return the letter of the start index
        return letters[start]
