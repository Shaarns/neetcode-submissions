# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev_group = dummy

        while True:
            kth = prev_group
            for i in range(k):
                kth = kth.next
                if kth is None:
                    return dummy.next

            group_start = prev_group.next
            next_group = kth.next
            prev = next_group
            curr = group_start

            while curr and curr != next_group:
                next_node = curr.next
                curr.next = prev 
                prev  = curr
                curr = next_node

            prev_group.next = kth
            prev_group = group_start

        return dummy.next
        

            

