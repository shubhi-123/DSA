# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#two people running around a circular track. One runs twice as fast, so eventually they must meet.

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast=head
        slow=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False