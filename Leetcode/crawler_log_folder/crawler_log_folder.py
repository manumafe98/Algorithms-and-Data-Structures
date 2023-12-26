from typing import List

# Slower runtime but better usage of memory
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack_array = []

        for command in logs:
            if command == "../":
                if len(stack_array) != 0:
                    stack_array.pop()
                else:
                    pass
            elif command == "./":
                pass
            else:
                stack_array.append(command)
        
        return len(stack_array)

# Better runtime but more memory usage

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        res = 0
        
        for i in logs:
            if i == '../' and res > 0:
                res -= 1
            elif i != './' and i != '../':
                res += 1
                
        return res
