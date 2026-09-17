class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # happy case
        # nums = [1,2,3,4], target = 3
        # output: [1,2]

        # edge case
        # nums = [1,-1,2,3,4], target = 3
        # output: [1,3]

        # brute force O(n^2)
        # forward backward two pointer approach

        l, r = 0, len(numbers) - 1

        while l < r:

            sum = numbers[l] + numbers[r]
            if  sum == target:
                return [l + 1, r + 1]

            elif sum > target:
                r -= 1

            else:
                l += 1

                

        