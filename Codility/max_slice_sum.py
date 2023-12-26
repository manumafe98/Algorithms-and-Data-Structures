"""
A non-empty array A consisting of N integers is given. 
A pair of integers (P, Q), such that 0 ≤ P ≤ Q < N, is called a slice of array A. 
The sum of a slice (P, Q) is the total of A[P] + A[P+1] + ... + A[Q].

Write a function:

def solution(A)

that, given an array A consisting of N integers, returns the maximum sum of any slice of A.

For example, given array A such that:

A[0] = 3  A[1] = 2  A[2] = -6
A[3] = 4  A[4] = 0
the function should return 5 because:

(3, 4) is a slice of A that has sum 4,
(2, 2) is a slice of A that has sum −6,
(0, 1) is a slice of A that has sum 5,
no other slice of A has sum greater than (0, 1).
Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..1,000,000];
each element of array A is an integer within the range [−1,000,000..1,000,000];
the result will be an integer within the range [−2,147,483,648..2,147,483,647].
"""

def solution(A):

    # We define max_value and sum as the first element in the array, because if we set the value as 0
    # Then the possible negatives outcomes woul throw 0 instead
    # Then we iterate over all the elements starting from index 1
    max_value = A[0]
    sum = A[0]

    for val in A[1:]:
        # Mas value holds the last sum
        max_value = max(val, max_value + val)
        # And then we compare it to the last maximum sum
        sum = max(sum, max_value)

    return sum
