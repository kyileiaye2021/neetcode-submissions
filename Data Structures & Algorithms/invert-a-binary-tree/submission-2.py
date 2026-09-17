# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invert(self, root):
        if not root:
            return None

        root.left, root.right = root.right, root.left

        if root.left:
            self.invert(root.left)
        if root.right:
            self.invert(root.right)

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #      3
        #     / \
        #  null.  1
        #       3
        #      / \
        #     1.  null
        # edge case: if tree is none, return none
        
        # base case: if both left and right nodes are null, return 
        # go to left and right nodes
        # swap left and right nodes

        if not root:
            return None

        self.invert(root)
        return root

    



        