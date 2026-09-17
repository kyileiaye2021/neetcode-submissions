class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # temp = [2, 3, 5]
        # res = [1, 1, 0]

        # temp = [2, 1, 3]
        # res = [2, 1, 0]

        # temp = [3, 2, 1]
        # res = [0, 0, 0]

        # temp = [1]
        # res = [0]

        # stack
        # append the ele until we meet the higher ele
        # while the ele in stack is less than the curr num and the stack is not empty
        #   count the num and assign that num to the curr arr?
        #   pop out the ele 

        res = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):

            while stack and temp > stack[-1][0]:
                t_ele, indx = stack.pop()
                res[indx] = i - indx

            stack.append((temp, i))

        return res

             

