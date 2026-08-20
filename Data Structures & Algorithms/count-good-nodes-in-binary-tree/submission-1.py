# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def search(node, greatest_val):
            if not node: return 0

            count = 0

            if node.val >= greatest_val:
                count += 1

            greatest_val = max(node.val, greatest_val)

            count += search(node.left, greatest_val)
            count += search(node.right, greatest_val)

            return count

        return search(root, float('-inf'))
