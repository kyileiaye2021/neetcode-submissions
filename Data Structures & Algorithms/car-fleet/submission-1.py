class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # iterate thru the pos
        #   find the hrs for each car to reach the des

        # sort the hour arr
        # iterate the hour arr
        #   check if the hour is not equal to prev hour
        #       increment our count

     
        # hashmap for pos: speed
        # sort the hashmap based on the position of the car in descending
        # iterate thru the hashmap
        #   find the hour for each car
        #   put it in the stack
        #   if the last ele is less than the second last ele
        #       pop the sec last ele
        # return the size of the stack

        pos_speed_map = {}
        for i, pos in enumerate(position):
            pos_speed_map[pos] = speed[i]

        # pos_speed_map = sorted(pos_speed_map.items(), reverse=True)
        # print(pos_speed_map)

        pos_speed_map = {key: val for key, val in sorted(pos_speed_map.items(), reverse=True)}
        print(pos_speed_map)

        stack = []
        for pos, speed in pos_speed_map.items():
            cur_hr = (target - pos) / speed
            stack.append(cur_hr)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)
