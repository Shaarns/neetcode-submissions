# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root: return None

        max_sum = root.val

        def dfs(root):
            nonlocal max_sum

            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)
            leftMax = max(left, 0)
            rightMax = max(right, 0)

            max_sum = max(max_sum, leftMax + rightMax + root.val)

            return root.val + max(leftMax, rightMax)

        dfs(root)
        return max_sum



        