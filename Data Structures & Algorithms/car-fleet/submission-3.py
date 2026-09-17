class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # happy case
        # Input: target = 10, position = [4,1,0,7], speed = [2,2,1,1]
        # Output: 3

        # target = 10, position = [1,4], speed = [3,2]
        #Output: 1

        # target = 10, position = [1], speed = [5]
        # output - 1

        # find the dist between current pos to des
        # find the hours it takes to travel that distance
        # iterate the pos
        #   subtract the curr ith pos from target
        #   divide the curr dist by curr speed i
        #   add the curr hour to the res set
        # return len(res)

        temp = sorted([(position[i], speed[i]) for i in range(len(position))])
    
        stack = []
        for i in range(len(temp) - 1, -1, -1):
            pos, sp = temp[i]
            dist = target - pos
            hr = dist / sp
            
            if stack:
                if stack[-1] < hr:
                    stack.append(hr)

            else:
                stack.append(hr)          

        return len(stack)

