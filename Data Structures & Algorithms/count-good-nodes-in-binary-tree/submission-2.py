# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root, count, prev):
        if not root:
            return

        print(f"root val: {root.val}")
        if root.val >= prev:
            print("increment the count")
            prev = root.val
            count[0] += 1

        self.dfs(root.left, count, prev)
        self.dfs(root.right, count, prev)

        # dfs func
        # if root is none
        #   return 
        # check if the curr val is greater than the prev val
        #   set curr val as max val so far
        #   increment the count
        # go to left and right subtree

    def goodNodes(self, root: TreeNode) -> int:
        # keep track of the max val in the binary tree
        # base case
        # prev val = smallest num
        # count = [0]
        # if root is none: return 0
        # call dfs on the root with prev val
        prev = float('-inf')
        count = [0]
        if not root:
            return 0
        self.dfs(root, count, prev)
        return count[0]

