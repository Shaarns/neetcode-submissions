# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalanced = [True]

        def height(root):
            if not root: return 0

            left = height(root.left)
            if isBalanced[0] == False:
                return 0
            right = height(root.right)

            if(abs(left - right) > 1):
                isBalanced[0] = False
                return 0

            return 1 + max(left, right)

        height(root)
        return isBalanced[0]