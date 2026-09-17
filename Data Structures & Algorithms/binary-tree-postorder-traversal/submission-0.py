# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal_helper(self, root, res_lst):
        # base case
        if not root:
            return res_lst

        # left
        self.postorderTraversal_helper(root.left, res_lst)

        # right
        self.postorderTraversal_helper(root.right, res_lst)

        # root
        res_lst.append(root.val)

        return res_lst

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        return self.postorderTraversal_helper(root, res)
        