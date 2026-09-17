class Solution:
    def findMin(self, nums: List[int]) -> int:
        # nums = []

        # sort the arry and return the first ele --> O(n^2)
        # iterate thru the arr and check if the ele is >1 greater than prev --> O(n)
        # partition with pointers and compare the smallest two pointer ele
        
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1

        return res