# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root, res):
        if not root:
            return 0
        
        left = max(0, self.dfs(root.left, res))
        right = max(0, self.dfs(root.right, res))

        res[0] = max(res[0], (left + right + root.val))
        return root.val + max(left, right)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # simiilar to max depth problem
        # post order traversal
        # go to left and right subtree and get max summ between them
        # add the max sum to the root val 
        # if the sume becomes neg, reset to 0
        res = [root.val]
        tree = self.dfs(root, res)
        return res[0]

