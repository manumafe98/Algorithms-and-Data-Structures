from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# This solutions uses a hashmap so its Memory is O(N)
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current = head
        nodes_dict = dict()

        while current and current.next:
            if current in nodes_dict:
                return True
            else:
                nodes_dict[current] = True
            
            current = current.next
        
        return False

# You can solve it like this instead that uses O(1) memory
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # This solution requires two pointers 
        slow = head
        fast = head

        # One that moves 1 space at a time and other that moves twice at a time
        # So the only way that the slow meets the fast is that exists a cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
