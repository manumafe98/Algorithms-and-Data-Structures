# We apply fibonacci logic
# 1 2 3 4 5 6 (stairs)
# 1 2 3 5 8 13 (combinations) 

class Solution:
    def climbStairs(self, n: int) -> int:
            if n <= 2:
                return n
            
            prev1 = 1
            prev2 = 2
            curr = 0
            
            # We start the iteration in 2 because we covered that cases in the if
            for _ in range(2, n):
                # We assign current to the sum of the previous
                curr = prev1 + prev2
                # and then update the previous values
                prev1 = prev2
                prev2 = curr
            return curr
