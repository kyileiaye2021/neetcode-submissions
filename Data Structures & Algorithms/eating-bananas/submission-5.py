import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Happy cases
        # input: piles = [1,2,3], h = 4
        # output: 3 [1,1,1]
        # 1 [1,2,3] not possible
        # 2 [1,1, 2] possible

        # input: piles = [20, 13, 15], h = 5
        # output: 20

        # Edge case
        # input: piles = [24], h =3
        # output: 24

        # need to find an int val to divide every ele in the list
        # get total division 
        # check if that total division is less than or equal h
        
        # keep track of the min eating rate (min total division)

        # Brute force - O(n^2)
        # Sort and iterate thru the list - O(n^2logn)


        # min_total_division = 0
        # min_res = piles[0]
        # for i in range(len(piles)):
        #     total_division = 0
        #     for j in range(len(piles)):
        #         division = math.ceil(piles[j] / piles[i])
        #         total_division += division
        #     print(total_division)
        #     if total_division <= h:
        #         if total_division > min_total_division:
        #             min_res = piles[i]
        #             print("min_res updated")
        #             min_total_division = total_division

        # return min_res  

        # check which integer is the min val to divide every ele in the list
        # and its total division is less than or equal to h val

        # check the integer val k from 1
        # max ele - the largest possible k that we can divide the ele
        # iterate from 1 to m and check the division - O(n*m)

        # binary search
        # l, r = 1, max val in list
        # find the middle val
        # total division = 0
        # iterate thru the list
        #   update total division
        # check if the total division is <= h
        #   update r
        # else:
        #   update l

        l, r = 1, max(piles)
        res = r

        while (l <= r):
            k = (l + r) // 2
            total_division = 0

            for ele in piles:
                division = math.ceil(ele / k)
                total_division += division 

            if total_division <= h:
                res = min(k, res)
                r = k - 1
            else:
                l = k + 1

        return res
