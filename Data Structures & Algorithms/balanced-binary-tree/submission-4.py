# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_balanced = [True]
        
        def tree(root):
            if root is None:
                return 0

            left = tree(root.left)
            right = tree(root.right)

            if abs(left - right) > 1:
                is_balanced[0] = False

            return 1 + max(left, right)

        tree(root)

        return is_balanced[0]