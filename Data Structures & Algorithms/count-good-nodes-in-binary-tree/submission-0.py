# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes_count = [0]

        def search(node, greatest_val):
            if not node: return 0

            if node.val >= greatest_val:
                good_nodes_count[0] += 1

            greatest_val = max(node.val, greatest_val)

            search(node.left, greatest_val)
            search(node.right, greatest_val)

        search(root, float('-inf'))

        return good_nodes_count[0]
