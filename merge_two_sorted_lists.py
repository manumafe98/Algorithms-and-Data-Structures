# Leetcode
"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy empty linked list
        dummy = ListNode()
        tail = dummy

        # iterate until both lists are empty
        while list1 and list2:
            #if the value of list 1 is smaller
            if list1.val < list2.val:
                # Add it to the tail of the dummy list and update the list1 value to the next one
                tail.next = list1
                list1 = list1.next
            else:
                # The same if list2 is smaller
                tail.next = list2
                list2 = list2.next
            # update the tail value
            tail = tail.next
        
        # Check if there are remaining values in one of the lists
        # because it can happend that 1 of the two its empty
        # so all the remaining items are appended to the tail
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
    
        return dummy.next
