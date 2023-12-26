class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # k = worst scenario
        minimun_operations = k

        for i in range(len(blocks)):
            # Calculate the amount of B between i and i+k
            # being k = 4 would be 0:4 
            b_count = blocks[i:i+k].count("B")
            # so if the count is equal to k we know we have 4 consecutive B so we have 0 operations
            if b_count >= k:
                return 0
            # else we calculate the minimun between minimun_operations and
            # the amount of whites in that block
            minimun_operations = min(minimun_operations, k - b_count)
        return minimun_operations
