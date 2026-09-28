class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # happy cases
        # temperatures = [30,38,30,36,35,40,28]
        #  [1,4,1,2,1,0,0]

        # temperatures = [22,21,20]
        # [0, 0, 0]

        # temp = [21,22,23]
        # [1,1,0]

        # edge cases
        # [40]
        # [0]

        # [9,9]
        # [0,0]

        # stack
        # res = [0] * len(temp)
        # iterate thru the ele
        #   if not stack
        #       add ele to the stack with index i
        #   else
        #       while stack
        #           if stack[-1][0] < curr ele
        #               pop the curr ele 
        #               res[stack[-1][1]] = curr index - stack[-1][1]
        # return res

        stack = []
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            
            if stack:
                while stack:
                    if stack[-1][0] < t:
                        temp, idx = stack.pop()
                        res[idx] = i - idx
                    
                    else:
                        break

            stack.append((t, i))

        return res

