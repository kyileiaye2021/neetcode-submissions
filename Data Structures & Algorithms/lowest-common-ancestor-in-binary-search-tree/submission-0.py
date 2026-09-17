# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Happy case
        # root :5
        #      / \
        #     3    8
        #    / \  / \
        #   1  4 7   9
        #    \
        #      2
        # p: 3, q = 8
        # 5

        # root: 5
        #      / \
        #     3    8
        #    / \  / \
        #   1  4 7   9
        #    \
        #      2
        # p: 2, q =4
        # output: 3

        # root: 5
        #      / \
        #     3    8
        #    / \  / \
        #   1  4 7   9
        #    \
        #      2
        # p: 9, q = 1
        # output: 5

        # edge cases
        # root: 5
        #      / \
        #     3    8
        # p: 5, q = 3
        # output: 5


        # DFS 
        # if p and q are greater than root
        #   go to right
        # if p and q are less than root
        #   go to left
        # else: return root 
        # (if there is a split in node [p is greater than node n q is less than node --> split is LCA])
        # if one of p or q nodes is same as root, return root as well

        curr = root

        while curr:
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else: 
                return curr