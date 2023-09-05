# Codility

"""
An integer M and a non-empty array A consisting of N non-negative integers are given. 
All integers in array A are less than or equal to M.

A pair of integers (P, Q), such that 0 ≤ P ≤ Q < N, 
is called a slice of array A. The slice consists of the elements A[P], A[P + 1], ..., A[Q]. 
A distinct slice is a slice consisting of only unique numbers. 
That is, no individual number occurs more than once in the slice.

For example, consider integer M = 6 and array A such that:

    A[0] = 3
    A[1] = 4
    A[2] = 5
    A[3] = 5
    A[4] = 2
There are exactly nine distinct slices: (0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2), (3, 3), (3, 4) and (4, 4).

The goal is to calculate the number of distinct slices.

Write a function:

def solution(M, A)

that, given an integer M and a non-empty array A consisting of N integers, returns the number of distinct slices.

If the number of distinct slices is greater than 1,000,000,000, the function should return 1,000,000,000.

For example, given integer M = 6 and array A such that:

    A[0] = 3
    A[1] = 4
    A[2] = 5
    A[3] = 5
    A[4] = 2
the function should return 9, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
M is an integer within the range [0..100,000];
each element of array A is an integer within the range [0..M].
"""

# Time complexity: O(N * (N + M))
def solution(M, A):
    unique_array = []
    slices = 0

    for i in range(len(A)):
        front = i
        while front < len(A) and A[front] not in unique_array:
            unique_array.append(A[front])
            front += 1
            slices += 1
        unique_array = []
    
    if slices >  1000000000:
        return 1000000000
    else:
        return slices

# Time complexity: O(N)
def solution(M, A):
    unique_dict = {}
    slices = 0
    front = 0

    for back in range(len(A)):
        while front < len(A) and A[front] not in unique_dict:
            unique_dict[A[front]] = True
            front += 1
            # We increment the 'slices' count by the length of the current slice 
            # (front - back) whenever a new slice is found. This ensures that we count all the valid slices correctly.
            slices += front - back
            if slices > 1000000000:
                return 1000000000

        # Instead of resetting the value we remove the current back value
        unique_dict.pop(A[back])

    return slices