class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # happy cases
        # [1,4,3,2], h = 9
        # 2

        # [1,2,3], h = 3
        # 3

        # [25, 10, 23, 4], h = 4
        # 25

        # edge cases
        # [8], h = 4
        # 2
        # 
        # rate inversely proportional to hour

        # rate = 1
        # total hr = sum(piles)
        # while total hr > h:
        #   rate += 1
        #   total hr = 0
        #   for each ele
        #       total hr += (divide each pile // rate)
        # 
        # return rate
        # O(k*n)

        # rate - 1,2,3,4, ...
        # sorted ascending order

        # binary search
        # rate - 1 ... max ele in piles
        # min rate = float (inf)
        # l = 1
        # r = max ele
        # while l <= r:
        #   mid rate = (l + r) // 2
        #   total hr = 0
        #   for each p in piles
        #       total hr += ceil(p // mid rate)
        #   if total hr == h
        #       return mid rate
        #   elif total hr > h:
        #       l = mid rate + 1
        #   else:
        #       min rate = min(min rate, mid rate)
        #       r = mid rate -1
        # return min rate


        min_rate = float('inf')
        l = 1
        r = max(piles)
        while l <= r:
            mid_rate = (l + r) // 2
            total = 0

            for p in piles:
                total += math.ceil(p / mid_rate)

            if total > h:
                l = mid_rate + 1
            
            else:
                min_rate = min(min_rate, mid_rate)
                r = mid_rate - 1
            
        return min_rate

