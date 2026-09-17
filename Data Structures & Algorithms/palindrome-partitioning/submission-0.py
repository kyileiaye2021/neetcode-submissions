class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # happy 
        # s = "aab"
        # output: [['a', 'a', 'b'], ['aa', 'b']] 

        # s = "aa"
        # output: [['a', 'a'], ['aa']]

        # edge cases
        # s = "b"
        # output: [['b']]

        # backtracking
        # base case
        # index =0
        # when i hits the len of s:
        #   add the temp list to res
        #   return

        # for j loop to iterate thru the ele (starting from ith pos)
        #   do like a sub string [i:j]
        #   check if that sub string is a panlindrome
        #       add the substr to temp list
        #       call backtrack func on j + 1
        #       pop the ele from the temp list

        # call backtrack on the 0
        res = []
        temp = []

        def is_panlindrome(s,l,r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def dfs(i):
            # base case
            if i >= len(s):
                res.append(temp.copy())
                return

            for j in range(i, len(s)):
                if is_panlindrome(s, i, j):
                    temp.append(s[i:j+1])
                    dfs(j + 1)
                    temp.pop()
        dfs(0)
        return res


