# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # happy cases 
        #       3
        #      / \
        #     2.  1

        #      3
        #     / \
        #    1    2

        # edge cases
        # input: null
        #  output: null

        # input: 3
        # output: 3

        # input ; only one child
        #       3
        #      / \
        #     4.  null

        #       3
        #      / \
        #   null   4

        # goal: to switch the children in each node
        # DFS
        # base case: if the root node is none, return null
        # in each node, we have to swap the left and right node
        # go to the left subtree
        # go to the right subtree


        # base case
        if not root:
            return None

        # swap the two children
        root.left, root.right = root.right, root.left

        # go to left subtree
        self.invertTree(root.left)

        # go to right subtree
        self.invertTree(root.right)
        return root


