class Solution:
    def removeDuplicates(self, s: str) -> str:
        char_stack = []

        for char in s:
            if len(char_stack) == 0:
                char_stack.append(char)
            elif char == char_stack[-1]:
                char_stack.pop(-1)
            else:
                char_stack.append(char)
        return "".join(char_stack)
