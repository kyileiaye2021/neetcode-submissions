class Solution:
    def checkValidString(self, s: str) -> bool:

        # stack to store the open parenthesis
        # count = 0
        # iterate thru the chars
        #   if it's open paren, put it in the stack
        #   elif it's *, increment count
        #   else
        #       check if the last ele in the stack is open
        #           pop the stack
        #       else
        #           check if the count > 0
        #               pop the stack 
        #           else
        #               return False
        # return True

        star_stack = []
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)

            elif s[i] == '*':
                star_stack.append(i)

            else:
                if stack:
                    stack.pop()

                elif star_stack:
                    star_stack.pop()

                else:
                    return False

        while stack and star_stack:
            if stack[-1] < star_stack[-1]:
                stack.pop()
                star_stack.pop()

            else:
                return False

    
        return True if len(stack) == 0 else False
        