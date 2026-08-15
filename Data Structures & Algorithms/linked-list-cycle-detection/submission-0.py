# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited_nodes = set()

        curr = head
        while curr:
            visited_nodes.add(curr)
            curr = curr.next
            if curr in visited_nodes:
                return True
            print(curr)

        print(visited_nodes)

        return False