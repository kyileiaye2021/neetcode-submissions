class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # hashmap {digit: [chars]}
        #.  A
        # /    \
        # D     E
        # 

        # backtrack

        # if i == numo of digits
        #   add the curr path copy to the res list
        #   return 

        #    iterate thru (j) each char of curr digit i
        #       add the curr char to the curr_path 
        #       call backtrack on the next digit (i + 1)
        #       pop the curr char from the curr_path
        #       

        # res list
        # call backtrack func with i = 0 and curr_path set and res list
        # return res listc
        if len(digits) == 0:
            return []
        digit_map = {'2': ['A', 'B','C'],
                     '3': ['D', 'E', 'F'],
                     '4': ['G', 'H', 'I'], 
                     '5': ['J', 'K', 'L'],
                     '6': ['M', 'N', 'O'],
                     '7': ["P", 'Q', 'R', 'S'],
                     '8': ['T', 'U', 'V'],
                     '9': ['W','X', 'Y', 'Z']}
        res = []
        curr_lst = []

        # backtrack
        def backtrack(i, curr_lst):
            # base case
            if i == len(digits):
                curr_lst_copy = curr_lst.copy()
                res.append(''.join(curr_lst_copy))
                return 


            for j in range(len(digit_map[digits[i]])):
                curr_lst.append(digit_map[digits[i]][j].lower())

                # call the char on next level
                backtrack(i + 1, curr_lst)

                curr_lst.pop()

        backtrack(0, curr_lst)
        return res


