class Solution:
    def trap(self, height: List[int]) -> int:
        # prefix and postfix max

        # need to calculate how much water can be in each bar
        # water can be contained by the amount of (min val of left_max, right_max) - curr_bar heights

        # first need to know the max height from left and right
        # calculate how much water can be contained

        if len(height) == 0:
            return 0
        left_max = [0] * len(height)
        right_max = [0] * len(height)
        water = [0] * len(height)
        sum = 0

        left_max[0] = height[0]
        for i in range(1, len(height)):
            left_max[i] = max(left_max[i - 1], height[i])


        right_max[len(height)-1] = height[len(height)-1]
        for i in range(len(height)-2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        for i in range(len(height)):
            water[i] = min(left_max[i], right_max[i]) - height[i]
            if water[i] < 0:
                water[i] = 0

        for i in range(len(height)):
            sum += water[i]

        return sum

        

