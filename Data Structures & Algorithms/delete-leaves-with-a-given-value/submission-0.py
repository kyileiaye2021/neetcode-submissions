# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, target):
        if not root:
            return root

        root.left = self.dfs(root.left, target)
        root.right = self.dfs(root.right, target)

        if not root.left and not root.right:
            if root.val == target:
                return None
        return root

            
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        # dfs  (post order) left -> right --> root
        # if the node is empty, return []
        # if the node is leaf node, 
        #   check if the node val is equal to target
        #       delete the node and go back to the parent
        #   else:
        #       return 
        # if not --> go to the children nodes

        return self.dfs(root, target)