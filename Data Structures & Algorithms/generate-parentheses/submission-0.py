class Solution:
    # if open == close == n --> return 
    # if open < n --> can add more open
    # if close < open --> can add more close
    def backtrack(self, openN, closeN, n, res, stack):
        if openN == closeN == n:
            res.append(''.join(stack))
            return 
        
        if openN < n:
            stack.append('(')
            self.backtrack(openN + 1, closeN, n, res, stack)
            stack.pop()

        if closeN < openN:
            stack.append(')')
            self.backtrack(openN, closeN + 1, n, res, stack)
            stack.pop()
        

    def generateParenthesis(self, n: int) -> List[str]:
        # stack
        # input: n = 1
        # output: ["()"]

        # input: n = 2
        # output: ["()()", "(())"]

        # input: n = 3
        # output: ["()()()", "(())()", "()(())", "((()))", "(()())"]
        res = [] 
        stack = []
        self.backtrack(0, 0, n, res, stack)
        return res





        
        