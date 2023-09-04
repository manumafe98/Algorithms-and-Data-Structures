# Codility
"""
Two positive integers N and M are given. 
Integer N represents the number of chocolates arranged in a circle, numbered from 0 to N − 1.

You start to eat the chocolates. After eating a chocolate you leave only a wrapper.

You begin with eating chocolate number 0. 
Then you omit the next M − 1 chocolates or wrappers on the circle, and eat the following one.

More precisely, if you ate chocolate number X, 
then you will next eat the chocolate with number (X + M) modulo N (remainder of division).

You stop eating when you encounter an empty wrapper.

For example, given integers N = 10 and M = 4. You will eat the following chocolates: 0, 4, 8, 2, 6.

The goal is to count the number of chocolates that you will eat, following the above rules.

Write a function:

def solution(N, M)

that, given two positive integers N and M, returns the number of chocolates that you will eat.

For example, given integers N = 10 and M = 4. the function should return 5, as explained above.

Write an efficient algorithm for the following assumptions:

N and M are integers within the range [1..1,000,000,000].
"""

# O(N) solution

def solution(N, M):
    temp_val = 0
    count = 0

    while temp_val != N:
        temp_val += M
        count += 1
        if temp_val > N:
            temp_val -= N
    return count

# O(log(N + M))

# With this helper function we obtain the greatest common divisor
def helper(a, b):
    if a % b == 0:
        return b
    else:
        return helper(b, a % b)

# Then with the greatest common divisor we can obtain the least common multiple of both numbers
# with the forumula a * b / gcd
# And finally the iterations would be the lcm / b 
def solution(N, M):
    gcd = helper(N, M)

    lcm = N * M / gcd
    
    return int(lcm / M)
