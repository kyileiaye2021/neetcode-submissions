class Solution:
    def children(self, code):
        res = []

        for i in range(4):

            # add 
            digit = (int(code[i])+ 1) % 10
            next_code = code[:i] + str(digit) + code[i + 1:]
            res.append(next_code)

            # subtract
            digit = ((int(code[i]) - 1) + 10) % 10
            next_code = code[:i] + str(digit) + code[i + 1:]
            res.append(next_code)

        return res

    def openLock(self, deadends: List[str], target: str) -> int:
        # bfs
        # add '0000' to queue along with 0 turn

        # how to find the child of each code
        # iterate thru each digit in the code
        #   add by 1 -> digit + 1 % 10 
        #   subtract by 1 -> (digit - 1 + 10) % 10

        # until the queue is empty
        #   pop out the code
        #   if the code is equal to target -> return turns
        #   go to its other possible child
        #   if the child is not visited:
        #       if the child is not in the deadend list
        #           add the child to the queue
        #       else:
        #           return -1
        # return -1

        if '0000' in deadends:
            return -1
        
        visited = set(deadends)
        queue = deque()
        queue.append(('0000', 0))

        while queue:
            code, turns = queue.popleft()

            if code == target:
                return turns

            for child in self.children(code):
                if child not in visited:
                    visited.add(child)
                    queue.append((child, turns + 1))


        return -1


