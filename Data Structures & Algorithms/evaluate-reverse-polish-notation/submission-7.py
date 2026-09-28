class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # stack
        
        operators = []
        operands = set(["+", "-", "*", "/"])

        for t in tokens:
            if t not in operands:
                operators.append(int(t))

            else:
                if operators:
                    second = operators.pop()
                    first = operators.pop()
                    if t == '+':
                        res = first + second
                    elif t == '-':
                        res = first - second
                    elif t == '*':
                        res = first * second
                    else:
                        res = int(first / second)

                    operators.append(res)
        return operators[-1] if len(operators) == 1 else operators[0]



                    
