# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal_helper(self, root, res_lst):
        if not root:
            return res_lst
        self.inorderTraversal_helper(root.left, res_lst)

        res_lst.append(root.val)

        self.inorderTraversal_helper(root.right, res_lst)
        return res_lst

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        return self.inorderTraversal_helper(root, res)