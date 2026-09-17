# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root, total):
        # base case
        if not root:
            return 0
        
        left = max(0, self.dfs(root.left, total))
        right = max(0, self.dfs(root.right, total))
        total[0] = max(total[0], (root.val + left + right))

        return root.val + max(left, right)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        total = [root.val]
        height = self.dfs(root, total)
        return total[0]

        # find a path that has the max sum 

        # base case
        # if the node is none, return 0
        # total = max(total, curr + left subtree + right subtree)
        # since we have to find a single path, return height (1 + max(left ,right))


        