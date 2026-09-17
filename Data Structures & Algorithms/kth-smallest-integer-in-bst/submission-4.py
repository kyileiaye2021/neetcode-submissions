# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root, count, k):
        # if node becomes none return 
        # in order traversal
        # call left subtree until it reaches none
        # increment the count
        # check if the count becomes k
        #   return the curr node val
        # call right subtree until it reaches none
        if not root:
            return 
        
        left = self.dfs(root.left, count, k)

        count[0] += 1
        if count[0] == k:
            return root.val

        right = self.dfs(root.right, count, k)

        if left:
            return left
        else:
            return right
        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # dfs(root, count)
        return self.dfs(root, [0], k)