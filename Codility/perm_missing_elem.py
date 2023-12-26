"""
An array A consisting of N different integers is given. 
The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.

Your goal is to find that missing element.

Write a function:

def solution(A)

that, given an array A, returns the value of the missing element.

For example, given array A such that:

  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5
the function should return 4, as it is the missing element.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
the elements of A are all distinct;
each element of array A is an integer within the range [1..(N + 1)].
"""

# With len of the array plus 1 we calculate the greater number of the array
# then with this formula n * (n + 1) // 2 we calculate the expected arithmetic addtion of that greater num
# and finally we calculate the actual sum in the array substracting the actual value with the one we have


def solution(A):
    greater_number = len(A) + 1
    expected_sum = greater_number * (greater_number + 1) // 2
    actual_sum = 0
    for num in A:
        actual_sum += num
    return expected_sum - actual_sum