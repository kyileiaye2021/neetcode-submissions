class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # temp list
        # res list
        # map {"": []}


        # backtracking
        # dfs (i, list)
        #   if i >= len(map[digits[i]])
        #       return
        #   if the num of digit == len(temp) 
        #       combine all ele in the list to str 
        #       append the temp to the res
        #       return
        #   iterate thru the list from the start
        #       add the curr ele to the temp list
        #       dfs(i + 1,list)
        #       pop the curr ele from the temp list
        #       dfs(i + 1, list)
        # dfs(0, map[digits[0]])
        # return res

        res = []
        temp = []
        digit_map = {
            "2": ["a", "b", "c"],
            "3": ['d', 'e', 'f'],
            "4": ['g', 'h','i'],
            '5': ['j','k','l'],
            "6": ['m','n','o'],
            "7": ['p','q', 'r', 's'],
            '8': ['t','u', 'v'],
            '9': ['w','x', 'y','z']
        }

        def dfs(i):
            # base case

            if len(temp) == len(digits):
                temp_str = ''.join(temp)
                res.append(temp_str)
                print(res)
                return 

            for j in range(len(digit_map[digits[i]])):

                temp.append(digit_map[digits[i]][j])
                dfs(i + 1)

                temp.pop()
                # dfs(i + 1, digit_map[digits[i + 1]])

        if len(digits) == 0:
            return res
        dfs(0)
        return res



            


        