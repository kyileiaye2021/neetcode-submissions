class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        # hashmap 
        # res []
        # cur str = ''
        # dfs(i)
        # if i >= len(digits)
        #   add cur str to res
        #   return 

        # recursive case
        
        # for j in range(hashmap[digit[i]])
        #   add cur char to cur str
        #   dfs(i + 1)
        #   pop the cur char from cur str

        # dfs(0)
        # return res
        res = []
        cur_str = []
        if not digits:
            return res
        digit_map = {'2': ['a', 'b', 'c'],
                     '3': ['d', 'e', 'f'],
                     '4': ['g', 'h', 'i'],
                     '5': ['j', 'k', 'l'], 
                     '6': ['m', 'n', 'o'],
                     '7': ['p', 'q', 'r', 's'],
                     '8': ['t', 'u', 'v'],
                     '9': ['w', 'x', 'y', 'z']}

        def dfs(i):
            nonlocal cur_str
            if i >= len(digits):
                res.append(''.join(cur_str))
                return 

            # recursive case
            for j in digit_map[digits[i]]:
                cur_str.append(j)
                dfs(i + 1)
                cur_str.pop()

        dfs(0)
        return res


