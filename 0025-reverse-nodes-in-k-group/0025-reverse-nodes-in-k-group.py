# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def rev(head, k):
            prev=None
            current=head
            for _ in range(k):
                next_node=current.next
                current.next=prev
                prev=current
                current=next_node
            return prev, head, current
        current=head
        answer=None
        tail=None
        while current:
            temp=current
            cnt=0
            while temp and cnt<k:
                temp=temp.next
                cnt=cnt+1
            if cnt<k:
                if tail:
                    tail.next=current
                else:
                    answer=current
                break
            new_head, new_tail, current= rev(current, k)
            if answer is None:
                answer=new_head
            else:
                tail.next=new_head
            tail=new_tail
        return answer


