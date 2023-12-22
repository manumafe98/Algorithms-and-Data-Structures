"""
This is a demo task.

Write a function:

class Solution { public int solution(int[] A); }

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
"""
# This scores 77%
def solution(A):
    B = A[:]
    # Sort
    B.sort()

    # Eliminate duplicates and negatives
    unique_num_dict = dict()
    for num in B:
        if num < 0:
            pass
        else:
            if num in unique_num_dict:
                pass
            else:
                unique_num_dict[num] = True
    
    # convert dict in list
    unique_list = list(unique_num_dict)

    if len(unique_list) == 0:
        return 1
    else:
        tracking = 1
        for num in unique_list:
            if num != tracking:
                return tracking
            else:
                tracking += 1
        return unique_list[-1] +1

# 100% solution

def solution(A):
    A.sort()
    # If the last value is negative return 1
    if A[len(A) - 1] <= 0:
        return 1
    
    # Check if 1 exists in the sequence
    is_one = False
    for val in A:
        if val == 1:
            is_one = True

    if is_one == False:
        return 1

    # calculate the difference between the current number and the next one
    # if its more than 1 return that value
    for i in range(0, len(A) - 1):
        # A[i] > 0 its to avoid duplicates
        if A[i] > 0 and (A[i + 1] - A[i]) > 1:
            return A[i] + 1
    # if no missing numbers in the sequence then return the last one + 1
    return A[-1] + 1
