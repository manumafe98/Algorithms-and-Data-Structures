# Codility
"""
A positive integer D is a factor of a positive integer N if there exists an integer M such that N = D * M.

For example, 6 is a factor of 24, because M = 4 satisfies the above condition (24 = 6 * 4).

Write a function:

def solution(N)

that, given a positive integer N, returns the number of its factors.

For example, given N = 24, the function should return 8, 
because 24 has 8 factors, namely 1, 2, 3, 4, 6, 8, 12, 24. There are no other factors of 24.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..2,147,483,647].
"""
# 0(N) time complexity
def solution(N):
    i = 1
    factors = 0
    while i <= N:
        if N % i == 0:
            factors += 1
        i += 1
    return factors


# O(sqrt(N))
def solution(N):
    count = 0

    for i in range(1, int(N**0.5) + 1):
        if N % i == 0:
            count += 1
    if N == int(N**0.5) * int(N**0.5):
        return count * 2 -1
    else:
        return count * 2


# Codility lesson solution also O(sqrt(N))
def solution(n):
    i = 1
    result = 0
    while (i * i < n):
        if (n % i == 0):
            result += 2
        i += 1
    if (i * i == n):
        result += 1
    
    return result
