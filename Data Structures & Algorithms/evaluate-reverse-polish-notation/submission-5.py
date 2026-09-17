class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # ((1 + 2) * 3) - 4

        # 1
        # 1

        # 1 2 *
        # 2

        # - 
        # return 0

        # 1 + 
        # return 0

        # stack = [1, 2, *]
        # [1,2]
        # pop out the 2 ele
        # total = o1 operation o2
        # add the total stack
        stack = []

        i = 0
        res = 0
        while i < len(tokens):
            if tokens[i] == '+':
                stack.append(stack.pop() + stack.pop())
            
            elif tokens[i] == '-':
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)

            elif tokens[i] == '*':
                stack.append(stack.pop() * stack.pop())
            
            elif tokens[i] == '/':
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b / a))

            else:
                stack.append(int(tokens[i]))
            print(stack)
            i += 1

        return stack[0]
        

