# Leetcode
"""
Given a string s of lower and upper case English letters.

A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:

0 <= i <= s.length - 2
s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
To make the string good, you can choose two adjacent characters that make the string bad and remove them. 
You can keep doing this until the string becomes good.

Return the string after making it good. The answer is guaranteed to be unique under the given constraints.

Notice that an empty string is also good.

 

Example 1:

Input: s = "leEeetcode"
Output: "leetcode"
Explanation: In the first step, either you choose i = 1 or i = 2, 
both will result "leEeetcode" to be reduced to "leetcode".
Example 2:

Input: s = "abBAcC"
Output: ""
Explanation: We have many possible scenarios, and all lead to the same answer. For example:
"abBAcC" --> "aAcC" --> "cC" --> ""
"abBAcC" --> "abBA" --> "aA" --> ""
Example 3:

Input: s = "s"
Output: "s"
 

Constraints:

1 <= s.length <= 100
s contains only lower and upper case English letters.
"""

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
