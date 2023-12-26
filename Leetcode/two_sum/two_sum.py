from typing import List

# Time complexity = O(n)
# Space complexity = O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        # Loop all the array and add to the dictionary the number as key and index as value
        for indx, num in enumerate(nums):
            hashmap[num] = indx

        # Substract the number to the target and check if that complement is already in the hashmap
        for indx, num in enumerate(nums):
            complement = target - num
            if complement in hashmap and hashmap[complement] != indx:
                return [indx, hashmap[complement]]

solution = Solution()
print(solution.twoSum(nums=[2,7,11,15], target=9))
