# Codility
"""
An array A consisting of N integers is given. 
The dominator of array A is the value that occurs in more than half of the elements of A.

For example, consider array A such that

 A[0] = 3    A[1] = 4    A[2] =  3
 A[3] = 2    A[4] = 3    A[5] = -1
 A[6] = 3    A[7] = 3
The dominator of A is 3 because it occurs in 5 out of 8 elements of A 
(namely in those with indices 0, 2, 4, 6 and 7) and 5 is more than a half of 8.

Write a function

def solution(A)

that, given an array A consisting of N integers, 
returns index of any element of array A in which the dominator of A occurs. 
The function should return −1 if array A does not have a dominator.

For example, given array A such that

 A[0] = 3    A[1] = 4    A[2] =  3
 A[3] = 2    A[4] = 3    A[5] = -1
 A[6] = 3    A[7] = 3
the function may return 0, 2, 4, 6 or 7, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].
"""

def solution(A):
    val_dict = dict()

    if len(A) == 0:
        return -1

    # We loop over A and construct a dictionary with an array of indexes
    for idx, val in enumerate(A):
        if val in val_dict:
            val_dict[val].append(idx)
        else:
            val_dict[val] = [idx]

    # For every key in the dict we check the length of that array and if its greater than len(A) / 2
    # we return one of the values of that array
    for key in val_dict.keys():
        if len(val_dict[key]) > int(len(A) / 2):
            return val_dict[key][-1]
    
    return -1