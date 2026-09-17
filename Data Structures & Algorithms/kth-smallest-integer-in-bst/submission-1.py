# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root, k, arr):
        if not root:
            return 
        
        self.dfs(root.left, k, arr)

        arr.append(root.val)

        self.dfs(root.right, k, arr)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # traverse the tree in order and add them to the array
        # iterate thru the list upto k and return that ele

        # dfs (in order)
        arr = []
        self.dfs(root, k, arr)
        return arr[k - 1]