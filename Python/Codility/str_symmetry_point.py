"""
Write a function:

def solution(S)

that, given a string S, returns the index (counting from 0) of a character such that the part of the string 
to the left of that character is a reversal of the part of the string to its right. 
The function should return −1 if no such index exists.

Note: reversing an empty string (i.e. a string whose length is zero) gives an empty string.

For example, given a string:

"racecar"

the function should return 3, because the substring to the left of the character "e" at index 3 is "rac", 
and the one to the right is "car".

Given a string:

"x"

the function should return 0, because both substrings are empty.

Write an efficient algorithm for the following assumptions:

the length of string S is within the range [0..2,000,000].
"""

def solution(S):
    # If the number is even the result always is -1
    if len(S) % 2 == 0:
        return -1
    
    if len(S) == 1:
        return 0
    
    n = len(S) // 2
    
    count = -1
    ans = 0

    # Then we take the half rounded to the floor and start iterating
    for i in range(0, int(n)):
        if S[i] == S[count]:
            count -= 1
            ans += 1
        else:
            return -1
    return ans
