# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        #bubble sort technique will give TLE
        #use merge sort
        def findmiddle(head):
            slow=head
            fast=head
            while fast.next and fast.next.next:
                slow=slow.next
                fast=fast.next.next
            return slow

        def merge(head1, head2):
            dummy = ListNode(0)
            current = dummy
            while head1 and head2:
                if head1.val <= head2.val:
                    current.next = head1
                    head1 = head1.next
                else:
                    current.next = head2
                    head2 = head2.next
                current = current.next
            if head1:
                current.next = head1
            else:
                current.next = head2
            return dummy.next
        def ms(head):
            if not head or not head.next:
                return head
            middle = findmiddle(head)
            lefthead = head
            righthead = middle.next
            middle.next = None
            lefthead = ms(lefthead)
            righthead = ms(righthead)
            return merge(lefthead, righthead)
        return ms(head)