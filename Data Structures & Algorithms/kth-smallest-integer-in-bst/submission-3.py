# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0

        def in_order_t(root): #2: left = None
            nonlocal count

            if not root: return None

            left = in_order_t(root.left)

            if left is not None:
                return left

            count += 1

            if count == k:
                return root.val

            right = in_order_t(root.right)
            return right

        return in_order_t(root)
        
