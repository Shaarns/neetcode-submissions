"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return
        stk = [node]
        curr = node
        visited = set()
        old_to_new = {}

        while stk:
            node = stk.pop()
            if node in visited: continue
        
            visited.add(node)
            copy = Node(node.val)
            old_to_new[node] = copy

            for neigh in node.neighbors:
                stk.append(neigh)


        for old, new in old_to_new.items():
            for nei in old.neighbors:
                new.neighbors.append(old_to_new[nei])

        return old_to_new[curr]