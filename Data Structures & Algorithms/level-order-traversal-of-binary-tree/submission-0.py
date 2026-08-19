# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        q = collections.deque()
        q.append(root)
        res = []

        while q:
            level = []
            level_size = len(q)

            for _ in range(level_size):
                
                node = q.popleft()
                if not node: break

                level.append(node.val)
                
                if node and node.left:
                    left_node = node.left
                    q.append(left_node)
                if node and node.right:
                    right_node = node.right
                    q.append(right_node)

            res.append(level)

        return res
