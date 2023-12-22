"""
A string S consisting of N characters is called properly nested if:

S is empty;
S has the form "(U)" where U is a properly nested string;
S has the form "VW" where V and W are properly nested strings.
For example, string "(()(())())" is properly nested but string "())" isn't.

Write a function:

def solution(S)

that, given a string S consisting of N characters, returns 1 if string S is properly nested and 0 otherwise.

For example, given S = "(()(())())", the function should return 1 and given S = "())", 
the function should return 0, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..1,000,000];
string S is made only of the characters '(' and/or ')'.
"""

# Literally almost the same solution as brackets

def solution(S):
    open_bracket = "("
    bracket_array = []

    if len(S) == 0:
        return 1

    for char in S:
        if char == open_bracket:
            bracket_array.append(char)
        else:
            if len(bracket_array) == 0 or bracket_array[-1] != open_bracket:
                return 0
            else:
                bracket_array.pop()

    if len(bracket_array) == 0:
        return 1
    else:
        return 0
