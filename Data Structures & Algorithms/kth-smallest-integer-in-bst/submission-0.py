# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # need to find kth smallest element
        # inorder traversal
        # first go to the left subtree
        # check if curr count is less than or equal to k
        #   increment count by 1
        # if count == k
        #   return curr node val
        # go to the right subtree


    def kthSmallest_helper(self, root, k, count):
        if not root:
            return 
        
        left = self.kthSmallest_helper(root.left, k, count)

        if count[0] == k:
            count[0] += 1
            return root.val

        if count[0] <= k:
            count[0] += 1
        
        right = self.kthSmallest_helper(root.right, k, count)

        if left:
            return left
        if right:
            return right

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = [1]
        return self.kthSmallest_helper(root, k, count)
        
        