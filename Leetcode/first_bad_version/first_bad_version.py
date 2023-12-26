class Solution:

    def firstBadVersion(self, n: int) -> int:
        # The isBadVersion API is already defined for you in Leetcode.
        # def isBadVersion(version: int) -> bool:
        # Implemented to avoid errors, but it is not the actual code.
        def isBadVersion(num: int):
            return True
        
        first = 1
        last = n
        result = 0

        while first <= last:
            mid = int((last + first) // 2)
            if isBadVersion(mid):
                last = mid - 1
                result = mid
            else:
                first = mid + 1
        
        return result
