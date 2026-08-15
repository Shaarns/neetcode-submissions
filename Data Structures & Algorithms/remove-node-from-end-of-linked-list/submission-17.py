# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = slow = head

        count = 0
        while count < n:
            fast = fast.next
            count += 1

        while fast and fast.next:
            slow = slow.next
            fast = fast.next

        print("fast", fast)
        
        if head == slow and fast is None:
            head = slow.next
        elif slow.next and slow.next.next:
            slow.next = slow.next.next
        elif fast:
            slow.next = None

        return head

