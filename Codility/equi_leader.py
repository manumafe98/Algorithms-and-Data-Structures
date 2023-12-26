"""
A non-empty array A consisting of N integers is given.

The leader of this array is the value that occurs in more than half of the elements of A.

An equi leader is an index S such that 0 ≤ S < N − 1 and two sequences 
A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N − 1] have leaders of the same value.

For example, given array A such that:

    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2
we can find two equi leaders:

0, because sequences: (4) and (3, 4, 4, 4, 2) have the same leader, whose value is 4.
2, because sequences: (4, 3, 4) and (4, 4, 2) have the same leader, whose value is 4.
The goal is to count the number of equi leaders.

Write a function:

class Solution { public int solution(int[] A); }

that, given a non-empty array A consisting of N integers, returns the number of equi leaders.

For example, given:

    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2
the function should return 2, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000,000..1,000,000,000].
"""

def solution(A):
    # Calculating the dominator
    B = A[:]
    B.sort()

    count = 1
    leader = 0
    total_appearances = 0

    for idx, val in enumerate(B):
        if val != B[idx - 1]:
            count = 1
        else:
            count += 1
        
        if count > len(B) / 2:
            leader = val
            break
    
    # Getting the total of appearances of the leader
    for idx, val in enumerate(A):
        if val == leader:
            total_appearances += 1

    # Getting the equi_leaders of the array
    equi_leader = 0
    new_count = 0

    # with the new count and (total_appearances - new_count) 
    # we always know how many leaders are in both sides of the array
    for idx, val in enumerate(A):
        if val == leader:
            new_count += 1
        
        # to be the leader of an array the number of appearances of "the leader" should be greater of n/2
        # n being the length of the array, so the < works like in mathematic functions and to avoid trouble we pass it
        # multiplicating to the other side instead of (idx + 1)/2
        # (-idx - 1) represents the number of elements in the left side of the array
        # By the nature of the indexes they start with 0 but that already represents a value so that why we add the -1
        # The same goes to the idx + 1 because that represents the number of elements in that part of the array
        if idx + 1 < 2 * new_count and len(A) - idx - 1 < 2 * (total_appearances - new_count):
            equi_leader += 1
    
    return equi_leader
