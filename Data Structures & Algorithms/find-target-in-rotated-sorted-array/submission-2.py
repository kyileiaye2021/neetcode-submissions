class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # l, r = 0, end of the nums

        # while l <= r
        #   find mid index
        #   check if mid ele is target : return mid
        #   check if mid ele > l ele (mid is on the left side)
        #       if target > mid ele
        #           move l to mid + 1
        #       else
        #           if target < left ele
        #               move l to mid + 1
        #           else:
        #               move r to mid - 1
        #  if mid ele < l ele (mid is on the right side)
        #       if target < mid ele
        #           move r to mid - 1
        #       else:
        #           if target > r ele
        #               move r to mid - 1
        #           else
        #               move l to mid + 1
        #   return -1

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            print(nums[mid])
            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[l]:
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

