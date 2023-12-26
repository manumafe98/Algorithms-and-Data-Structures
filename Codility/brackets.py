"""
A string S consisting of N characters is considered to be properly nested if any of the following conditions is true:

S is empty;
S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
S has the form "VW" where V and W are properly nested strings.
For example, the string "{[()()]}" is properly nested but "([)()]" is not.

Write a function:

def solution(S)

that, given a string S consisting of N characters, returns 1 if S is properly nested and 0 otherwise.

For example, given S = "{[()()]}", the function should return 1 and given S = "([)()]", 
the function should return 0, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..200,000];
string S is made only of the following characters: '(', '{', '[', ']', '}' and/or ')'.
"""

def solution(S):
    # We define a empty stack to store the opening brackets
    stack = []
    opening_brackets = ["(", "[", "{"]
    closing_brackets = [")", "]", "}"]

    # If S is an empty string return 1
    if len(S) == 0:
        return 1

    for char in S:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            # If char is a closing bracket, and the stack is empty return 0
            # aswell if the last index in the stack is in a diferent index in opening/close brackets
            # that means that are different type of brackets and we return 0
            if len(stack) == 0 or opening_brackets.index(stack.pop()) != closing_brackets.index(char):
                return 0
    # if after the loop we have an empty stack we return 0 else it means that some type of bracket/brackets remain
    if len(stack) == 0:
        return 1
    else:
        return 0