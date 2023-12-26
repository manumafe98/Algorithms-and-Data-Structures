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
