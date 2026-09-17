class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # nums = [1,2,3,4], target = 3
        # output: [1,2]
    
        # nums = [1,2,3,4], target = 5
        # output: [2,3]

        # nums = [-8, -1, 1, 2], target = -9
        # output: [1, 3]

        # nums = [4,5], target = 9
        # output: 1,2

        # brute force - O(n^2)
        # hashmap - {ele: idx + 1} O(n) O(n)
        # binary search - two pointers at the end

        # l, r 
        # until l and r equal 
        #   check if the l ele + r ele is greater than target
        #       r -= 1
        #   else if sum is < target
        #       l += 1
        #   else
        #       return [l + 1, r + 1]
        
        l = 0
        r = len(numbers) - 1

        while l != r:
            sum = numbers[l] + numbers[r]
            if sum > target:
                r -= 1

            elif sum < target:
                l += 1

            else:
                return [l + 1, r + 1]
                
