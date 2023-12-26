from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # We define two pointers
        prev = None
        current = head

        while current:
            # We store the current.next temporarily so we dont loose the relation
            temp = current.next
            
            # We flip the pointer to previous
            current.next = prev

            # Then we update the values
            prev = current
            current = temp
        
        return prev        
