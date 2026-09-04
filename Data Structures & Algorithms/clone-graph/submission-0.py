"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        stack = []
        start = node
        visited = set()
        old_to_new = {}
        visited.add(node)
        
        copy = Node(node.val)
        old_to_new[node] = copy

        stack.append(node)

        while stack:
            node = stack.pop()

            for nei in node.neighbors:
                if nei not in visited:
                    old_to_new[nei] = Node(nei.val)
                    visited.add(nei)
                    stack.append(nei)

        for old, new in old_to_new.items():
            for nei in old.neighbors:
                new.neighbors.append(old_to_new[nei])

        return old_to_new[start]
                