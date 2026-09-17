# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # def dfs(self, root, k, arr):
    #     if not root:
    #         return 
        
    #     self.dfs(root.left, k, arr)

    #     arr.append(root.val)

    #     self.dfs(root.right, k, arr)

    def dfs(self, root, k, count):
        if not root:
            return

        left = self.dfs(root.left, k, count)

        count[0] += 1
        if count[0] == k:
            return root.val

        right = self.dfs(root.right, k, count)

        if left:
            return left

        if right:
            return right


    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # traverse the tree in order and add them to the array
        # iterate thru the list upto k and return that ele

        # dfs (in order)
        # arr = []
        # self.dfs(root, k, arr)
        # return arr[k - 1]
        count = [0]
        res = self.dfs(root, k, count)
        return res