class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # happy case
        # input: numbers = [1, 2,3,4], target = 3
        # output: [1, 2]

        # input: numbers = [1, 4], target =5
        # output: [1, 2]

        # two pointer 
        l, r = 0, len(numbers) - 1

        while l < r:

            sum = numbers[l] + numbers[r]

            if sum > target:
                r -= 1

            elif sum < target:
                l += 1

            else:
                return [l + 1, r + 1]

        

        