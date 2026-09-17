class Solution:
    def isValid(self, s: str) -> bool:
        # hashmap {closing: opening}
        # stack

        # iterate thru the s
        #   if it's open
        #       add it to stack
        #   else
        #       curr open - pop out the stack
        #       check if the corresponding opening in hashmap != curr open
        #           return false
        # return true

        map = {']':'[', '}':'{', ')':'('}
        open_stack = []

        for ele in s:
            if ele not in map:
                open_stack.append(ele)
            
            else:
                if len(open_stack) > 0:
                    curr_open = open_stack.pop()
                    if map[ele] != curr_open:
                        return False
                else:
                    return False

        return True if len(open_stack) == 0 else False

