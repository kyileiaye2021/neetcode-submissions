# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal_helper(self, root, res_lst):
        if not root:
            return res_lst
        # root
        res_lst.append(root.val)

        # left
        self.preorderTraversal_helper(root.left, res_lst)

        # right
        self.preorderTraversal_helper(root.right, res_lst)

        return res_lst

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        return self.preorderTraversal_helper(root, res)