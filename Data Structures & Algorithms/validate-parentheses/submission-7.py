class Solution:
    def isValid(self, s: str) -> bool:
        # pair of open and close param
        # stack
        # iterate thru the s
        #   if the curr char is open
        #       add it to the stack
        #   else
        #       check if the curr close is not pair with the last param in stack
        #           return False

        # return True
        map = {']': '[', ')':'(','}':'{'}

        stack = []

        for c in s:
            if c not in map:
                stack.append(c)
            
            else:
                if not stack:
                    return False

                elif stack and stack[-1] != map[c]:
                    return False

                else:
                    stack.pop()

        return True if not stack else False
