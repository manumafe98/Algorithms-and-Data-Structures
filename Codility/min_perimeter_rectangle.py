"""
An integer N is given, representing the area of some rectangle.

The area of a rectangle whose sides are of length A and B is A * B, and the perimeter is 2 * (A + B).

The goal is to find the minimal perimeter of any rectangle whose area equals N. 
The sides of this rectangle should be only integers.

For example, given integer N = 30, rectangles of area 30 are:

(1, 30), with a perimeter of 62,
(2, 15), with a perimeter of 34,
(3, 10), with a perimeter of 26,
(5, 6), with a perimeter of 22.
Write a function:

def solution(N)

that, given an integer N, returns the minimal perimeter of any rectangle whose area is exactly equal to N.

For example, given an integer N = 30, the function should return 22, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..1,000,000,000].
"""
def solution(N):
    i = 1
    # We define an absurd perimeter cause "N is an integer within the range [1..1,000,000,000]."
    perimeter = 300000000000000
    # We use the O(sqrt(N)) approach to only take on consideration the first divisors
    while i * i < N:
        if N % i == 0 and 2 * (( N / i) + i) < perimeter:
            perimeter = 2 * (( N / i) + i)
        i += 1
    # And then check for the cases that N is a perfect square root number (36)
    if i * i == N:
        perimeter = 2 * (( N / i) + i)
    return int(perimeter)
