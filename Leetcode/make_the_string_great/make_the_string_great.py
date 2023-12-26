class Solution:
    def makeGood(self, s: str) -> str:
        # We create a stack to hold the values
        char_stack = []

        # Then iterate over the string
        for char in s:
            # Edge case if the stack is empty
            if len(char_stack) == 0:
                char_stack.append(char)
            # Check if the char is equal as the last one in the stack and if is upper aswell
            elif char.isupper() and char.lower() == char_stack[-1]:
                char_stack.pop(-1)
            # Then do the same as before but if the char in the array is uppercase and the upcoming char lowecase
            elif char_stack[-1].isupper() and char == char_stack[-1].lower():
                char_stack.pop(-1)
            else:
                char_stack.append(char)
        
        return "".join(char_stack)
