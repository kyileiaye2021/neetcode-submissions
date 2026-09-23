class Solution:
    def findMin(self, nums: List[int]) -> int:
        # happy cases
        # nums = [3,4,5,6,1,2]
        # 1

        # nums = [4,5,6]
        # 4

        # nums = [6,7,1]
        # 1

        # edge cases
        # [-6,-1,1,2]
        # -6

        # [7,8,-1,0]
        # -1

        # [9]
        # 9

        # l , r
        # while l < r:
        #   if l ele < r ele:
        #       return l ele
        #   mid = l + r //2
        #   if mid ele > l ele
        #       l = mid + 1
        #   else:
        #       min n = mid ele
        #       r = mid - 1
        # return min n

        l = 0
        r = len(nums) - 1
        res = nums[0]
        while l <= r:
            if nums[l] <= nums[r]:
                res = min(res,nums[l])
                break

            mid = (l + r) // 2

            if nums[mid] >= nums[l]:
                l = mid + 1

            else:
                res = min(res, nums[mid])
                r = mid - 1

        return res
