"""
You have n coins and you want to build a staircase with these coins. 
The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.

 

Example 1:


Input: n = 5
Output: 2
Explanation: Because the 3rd row is incomplete, we return 2.
Example 2:


Input: n = 8
Output: 3
Explanation: Because the 4th row is incomplete, we return 3.
 

Constraints:

1 <= n <= 231 - 1
"""
# O(Log(n))
class Solution:
    def arrangeCoins(self, n: int) -> int:
        # Define our pointers
        start = 1
        end = n
        res = 0


        while start <= end:
            # Calcuate the mid of the pointers
            mid = (start + end) // 2
            # Math Gauss formula
            coins = (mid / 2) * (mid + 1)

            # If you need more coins to achieve that solution shift the end pointer to the left
            if coins > n:
                end = mid - 1
            else:
                # Else shift the start pointer to the right
                start = mid + 1
                # And update the current res
                res = max(mid, res)
        return res
    
# O(N)
class Solution:
    def arrangeCoins(self, n: int) -> int:
        count = 0
        num = 1

        while n >= 0:
            n = n - num
            num += 1
            count += 1
        
        return count - 1
