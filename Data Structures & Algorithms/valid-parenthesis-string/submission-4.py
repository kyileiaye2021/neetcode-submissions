class Solution:
    def checkValidString(self, s: str) -> bool:
        # 2 stacks
        # open = []
        # star = []

        # iterate thru s
        #   if '('
        #       add the curr idx to open
        #   elif '*'
        #       add the curr idx to star
        #   elif ')'
        #       if not open: return False
        #       else:
        #           pop the open

        # while open
        #   if last ele of open < last ele of star
        #       pop both open and star

        # return False if open else True

        open = []
        star = []

        for i, char in enumerate(s):
            if char == '(':
                open.append(i)

            elif char == '*':
                star.append(i)

            elif char == ')':
                if not open and not star:
                    return False

                elif not open:
                    star.pop()
                
                else:
                    open.pop()

            
        while open and star:
            if open[-1] < star[-1]:
                open.pop()
                star.pop()
            else:
                break

        return False if open else True

