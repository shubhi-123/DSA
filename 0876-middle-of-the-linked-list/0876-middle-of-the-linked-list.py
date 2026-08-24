# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cnt=0
        current=head
        while current:
            cnt=cnt+1
            current=current.next
        idx=cnt//2
        cnt=0
        current=head
        while cnt!=idx:
            cnt=cnt+1
            current=current.next
        return current

