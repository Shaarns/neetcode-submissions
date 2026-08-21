# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        res = 0

        def in_order_t(root):
            nonlocal count
            nonlocal res

            if not root: return 0


            in_order_t(root.left)

            count += 1
            if count == k:
                res = root.val
                return 

            in_order_t(root.right)

        in_order_t(root)
        return res
