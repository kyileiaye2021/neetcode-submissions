class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack
        # res
        # curr max = 1st temp
        # iterate thru the eles from 2nd ele
        #   if stack and curr_max < curr ele
        #       count = 0
        #       while stack
        #           pop out the ele from the stack
        #           increment count
        #           append left the count to the temp queue
        #       add the temp queue to res
        
        #   
        #    add the curr ele to the stack
        #    curr_max = max(curr_max, curr ele)

        # iterate thru the stack
        #   append 0 to res

        # return res

        res = [0] * len(temperatures)
        stack = []
        
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                t, idx = stack.pop()
                res[idx] = i - idx

            stack.append((temp, i))

        for temp, i in stack:
            res[i] = 0
            stack.pop()
        
        return res
            

        
