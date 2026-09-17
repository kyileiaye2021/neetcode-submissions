# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        res = []
        def dfs(root):
            if not root:
                res.append('N')
                return 

            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return ','.join(res)
            
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        vals = data.split(',')
        i = [0]

        def dfs(i):

            if vals[i[0]] == 'N':
                i[0] += 1
                return None

            node = TreeNode(int(vals[i[0]]))
            i[0] += 1
            node.left = dfs(i)
            node.right = dfs(i)
            return node

        return dfs(i)

       




