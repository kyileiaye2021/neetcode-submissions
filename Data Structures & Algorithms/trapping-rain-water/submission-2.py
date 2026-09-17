class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_left = [0] * n
        max_right = [0] * n
        min_num = [0] * n

        curr_l = 0
        for i, h in enumerate(height):
            max_left[i] = curr_l
            curr_l = max(curr_l, height[i])

        curr_r = 0
        for i in range(n-1, -1, -1):
            max_right[i] = curr_r
            curr_r = max(curr_r, height[i])

        for i in range(n):
            min_num[i] = min(max_left[i], max_right[i])

        res = 0
        for i, h in enumerate(height):
            if (min_num[i] - h) > 0:
                res += min_num[i] - h

        return res