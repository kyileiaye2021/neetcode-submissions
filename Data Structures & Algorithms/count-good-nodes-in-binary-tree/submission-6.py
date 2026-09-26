# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # count = 0
        # max = -inf
        # recur_good(root, max)
        # nonlocal count
        # if root = none: return
        # check if root.val > max:
        #   increment the count
        # go to left subtree
        # go to right subtree

        # recur_good(root, max)
        # return count

        count = 0
        max_val = float('-inf')
        def recur_good(root, max_val):
            nonlocal count

            if not root:
                return 

            if root.val >= max_val:
                count += 1
                max_val = root.val

            recur_good(root.left, max_val)
            recur_good(root.right, max_val)

        recur_good(root, max_val)
        return count
        