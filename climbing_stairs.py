# Leetcode

"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45
"""
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
