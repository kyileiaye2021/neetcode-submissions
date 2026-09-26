# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # inorder traversal
        # k 
        # kth_smallest
        # recur(root)
        # if not root:
        # return 
        # recur(root.left)
        # k -= 1
        # if k == 0
        #   kth_smallest = root.val
        #   return 
        # recur(root.right)

        # recur(root)

        kth_smallest = 0

        def recur_kthSmallest(root):
            nonlocal k 
            nonlocal kth_smallest

            if not root:
                return

            recur_kthSmallest(root.left)
            
            k -= 1
            if k == 0:
                kth_smallest = root.val
                return

            recur_kthSmallest(root.right)

        recur_kthSmallest(root)
        return kth_smallest

            
