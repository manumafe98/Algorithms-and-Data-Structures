
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
