# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # dfs
    # base case
    # if the node is None, return root
    # swap two children 
    # go to left and right subtree
    # return root

    def dfs(self, root):
        if not root:
            return root
        root.left, root.right = root.right, root.left
        root.left = self.dfs(root.left)
        root.right = self.dfs(root.right)
        return root
        
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        return self.dfs(root)
        