# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = l1
        curr2 = l2
        carry = 0
        head_new = new_node = ListNode()

        while curr or curr2 or carry:
            curr_val = 0
            curr2_val = 0

            if curr:
                curr_val = curr.val
                curr = curr.next

            if curr2:
                curr2_val = curr2.val
                curr2 = curr2.next

            total = curr_val + curr2_val + carry
            digit = total % 10
            carry = total // 10

            
            new_node_next = ListNode(digit)
            new_node.next = new_node_next
            new_node = new_node.next

        return head_new.next



            
