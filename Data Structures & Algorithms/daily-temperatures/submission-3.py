class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # happy cases
        # [30,38,30,36,35,40,28]
        # [1,4,1,2,1,0,0]


        # edge cases
        # [22,5,1]
        # [0,0,0]

        # [22]
        # 0

        # stack
        # as soon as we find the one greater than the last ele in the stack
        #   pop out the stack and put curr ele - popped ele in the idx of that popped ele
        #   do it until the last ele > the curr one

        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            curr_temperature = temperatures[i]
            while stack and stack[-1][1] < curr_temperature:
                idx, prev_temp = stack.pop()
                res[idx] = i - idx

            stack.append((i, t))

        return res



