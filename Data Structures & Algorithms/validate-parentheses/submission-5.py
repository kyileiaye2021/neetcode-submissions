class Solution:
    def isValid(self, s: str) -> bool:
        
        # happy casees
        # s = []
        # true

        # s = [{}]
        # true

        # s = []{}
        # true

        # edge cases
        # s = [
        # false

        # s = }
        # false

        # s = {]}
        # false

        # s = {[}
        # false

        # stack

        # itereat thru the brackets
        #   if open
        #       add the closed corresponding bracket to the stack
        #   else:
        #       check the last ele of stack == curr bracket
        #           pop the stack
        #       else: return false

        # return true if stack if empty

        brackets = {'[': ']', '{': '}', '(': ')'}
        closed = []

        for bracket in s:
            if bracket in brackets:
                closed.append(brackets[bracket])

            else:
                if closed and bracket == closed[-1]:
                    closed.pop()

                else:
                    return False

        return True if not closed else False

                




