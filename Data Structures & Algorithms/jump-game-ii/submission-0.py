class Solution:
    def jump(self, nums: List[int]) -> int:
        # jump var
        # two pointers l, r
        # until r reaches the end of the list
        #   l = ele next to r
        #   iterate thru the ele in the window 
        #       find the max dist we can go from the curr index
        #   jump will be incremented by 1

        l,r = 0, 0
        jump = 0

        while r < len(nums) - 1:
            jump += 1
            max_dist = 0

            for i in range(l, r + 1):
                curr_dist = i + nums[i]
                max_dist = max(max_dist, curr_dist)

            l = r + 1
            r = max_dist

        return jump 

