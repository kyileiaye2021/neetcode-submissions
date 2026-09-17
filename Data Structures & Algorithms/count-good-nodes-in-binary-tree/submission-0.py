# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # happy cases
    # input: root = [2,1,1,3, null, 1, 5]
    # output: 3

    # input: root = [1,2,-1,3,4]
    # output: 4

    # edge cases

    # input: root = [2]
    # output = 1

       # DFS we need to keep track of the max val so far
       # preorder traversal
       # base case: if the root is none, return 0
       # for each curr node, check if it is greater than max val
       #    update the max val
       #    increment the count by 1
       # go to the left and right subtree
    
    def goodNodes_helper(self, root, max_val, count):
        # base case
        if not root:
            return 0

        if root.val >= max_val:
            count[0] += 1
            max_val = max(max_val, root.val)

        self.goodNodes_helper(root.left, max_val, count)
        self.goodNodes_helper(root.right, max_val, count)

        return count[0]

    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        max_val = float("-inf")
        count = [0]
        return self.goodNodes_helper(root, max_val, count)
    



