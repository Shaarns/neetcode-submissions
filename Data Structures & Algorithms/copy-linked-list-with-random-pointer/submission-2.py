"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        original_to_new_map = {}

        curr = head
        head2 = list2 = Node(curr.val) if head else None
        original_to_new_map[curr] = list2
        
        while curr and curr.next and list2:
            curr = curr.next
            new_node = Node(curr.val)
            original_to_new_map[curr] = new_node
            list2.next = new_node
            list2 = list2.next

        curr = head
        curr2 = head2
        while curr and curr2:
            if curr.random == None:
                curr2.random = None

            new_node_next = original_to_new_map.get(curr.random)
            curr2.random = new_node_next

            curr = curr.next
            curr2 = curr2.next

        return head2


        