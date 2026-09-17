class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # happy case
        # nums = [4,5,6,1,2,3]
        # target = 2
        # output:4

        # nums = [4,5,6,1,2,3]
        # target = 5
        # output : 1

        # nums = [4,5,6,1,2,3]
        # target = 6
        # output: 2

        # edge cases
        # nums = [1,2,3,4]
        # target: 2
        # output: 1

        # nums = [2]
        # target = 5
        # output: -1

        # binary search
        # l, r
        # mid 
        # if mid > l pointer ele: # left portion
        #   if mid > target
        #       check if the target <= left pointer ele
        #           go to right portion
        #       else
        #           go to left portion
        #   else
        #       go to right portion

        # else # right portion
        #   if mid > target
        #       go to left portion
        #   else
        #       check if target > right ele
        #           go to left portion
        #       else
        #           go to right portion

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[l]: # left portion
                if target > nums[mid]: 
                    l = mid + 1
                else:
                    if target < nums[l]:
                        l = mid + 1

                    else:
                        r = mid - 1

            else:
                if target < nums[mid]:
                    r = mid - 1
                else:
                    if target > nums[r]:
                        r = mid - 1
                    else:
                        l = mid + 1

        return -1


