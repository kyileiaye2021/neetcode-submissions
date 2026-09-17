class Solution:
    def isValid(self, s: str) -> bool:
        # happy cases
        # input: s = '{}'
        # output: true

        # input: s = '{[]}'
        # output: true

        # edge cases
        # input: s = '[]]'
        # output: false

        # input: s = '('
        # output: false

        # input: s = '[(])'
        # output: false

        # stack
        # create a stack to store opening brackets
        # create a dict that pairs the closing bracket and opening bracket
        # iterate over the str
        #   check if the current char is opening or not
        #       put it on the stack
        #   else:
        #     check if the stack is not empty
        #       check the last ele in the stack is the opening bracket corresponding to the curr clsoing char
        #           remove the last ele from the stack
        #     else: return false
        # return true

        opening_stack = []
        bracket_dict = {']':'[', ')':'(', '}':'{'}

        for ele in s:
            if ele in bracket_dict.values():
                opening_stack.append(ele)
            else:
                if opening_stack:
                    last = opening_stack.pop()
                    if last != bracket_dict[ele]:
                        return False
                else:
                    return False
        
        if opening_stack:
            return False
        return True
