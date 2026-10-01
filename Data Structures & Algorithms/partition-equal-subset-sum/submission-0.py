class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        # recur(i, target)
        # base case
        #   if i > len(nums) or target < 0
        #       return False
        #   if target == 0
        #       return True

        # recursive case
        #   include = nums[i] + recur(i + 1, target - nums[i])
        #   exclude = recur(i + 1, target)
        #   return include and exclude

        total = sum(nums)
        if total % 2: # total == odd
            return False

        target = total // 2
        memo = {}

        def recur_partition(i, target):
            # base case
            if i >= len(nums) or target < 0:
                return False

            if target == 0:
                return True

            # recursive case
            if (i, target) in memo:
                return memo[(i, target)]

            include = recur_partition(i + 1, target - nums[i])
            exclude = recur_partition(i + 1, target)

            memo[(i, target)] = include or exclude
            return memo[(i, target)]

        return recur_partition(0, target)

