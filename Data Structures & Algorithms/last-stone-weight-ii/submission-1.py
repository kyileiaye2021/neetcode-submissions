class Solution:
    def minWeight(self, stones, target, i, total, memo):
        # dp recursion
        # base case
        # if the total becomes target
        #   return total - (sum - total)

        # cashing
        # if the min weight is stored in the dp memo at that ith position and total stage
        #   return min weight stored at that state

        # include = dp recursive on i + 1 and total + curr ith ele
        # exclude = dp recursive on i + 1 
        # store the min of include and exclude to the curr ith and total stage

        # return the min weight at that stage

        if total >= target or i >= len(stones):
            return abs(total - (sum(stones) - total))

        if (i, total) in memo:
            return memo[(i, total)]

        # in both cases, we have to go to next ele in the arr 
        include = self.minWeight(stones, target, i + 1, total + stones[i], memo)
        exclude = self.minWeight(stones, target, i + 1, total, memo)
        memo[(i, total)] = min(include, exclude)

        return memo[(i, total)]

    def lastStoneWeightII(self, stones: List[int]) -> int:

        # happy cases
        # input: stones = [2,4,1,5]
        # output: 0

        # input: stone == [2,4,1,5,6,3]
        # output: 1

        # input: [4,4,1,7,10]
        # output: 2

        # edge cases:
        # input: [2]
        # output: 2

        # input: [1,1]
        # output: 0

        # sort the arr - O(nlogn)
        # until the arr has only one ele
        #   pop the two ele from the end
        #   if x != y
        #       abs(x - y) and add it to the arr
        # return the one ele in the arr


        # heap  - nlog(n)
        # heapify the stones
        # until the heap is only one ele
        #   heappop the last two
        #   check if they are not equal
        #       heappush abs(y - x) to the heap

        # we have to find the min weight
        # we have to find two pairs whose diff can result in min weight

        # recursion brute force - O(2^n)
        # start from the i = 0 and combine with other eles and make paths 
        # then backtrack

        # dp
        # sum of the all n
        # half the sum 
        
        memo:Dict[Tuple[int, int]: int] = {}
        target = math.ceil(sum(stones) / 2)
        res = self.minWeight(stones, target, 0, 0, memo)
        print(memo)
        return res



    
        