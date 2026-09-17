# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root, count, max_val):
        if not root:
            return 
        
        if root.val >= max_val:
            count[0] += 1
            max_val = root.val

        self.dfs(root.left, count, max_val)
        self.dfs(root.right, count, max_val)
        
    def goodNodes(self, root: TreeNode) -> int:
        # dfs (root, count, max_val)
        # keep track of what val is the max so far in each level
        # if root none
        #   return 
        # check if the curr val >= max val 
        #   update count
        # update the max val with the curr val
        count = [0]
        max_val = float('-inf')
        self.dfs(root, count, max_val)
        return count[0]
        
        

        