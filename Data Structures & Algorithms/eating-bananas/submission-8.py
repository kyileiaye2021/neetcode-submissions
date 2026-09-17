class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # k val can be 1 uptoo max amount bananas in pile
        # k = [1 , ..., max(piles)]

        # min k 
        # iterate thru the k list
        #   iterate thru the piles
        #       curr hour = divide the bananas by the k
        #   add the total hour   
        #   if total hour < = h:
        #       keep track of k

        l = 1
        r = max(piles)
        res = r

        while l <= r:
            
            curr_hour = 0
            k = (l + r) // 2

            for p in piles:
                curr_hour += math.ceil(p / k)

            if curr_hour > h:
                l = k + 1

            elif curr_hour <= h:
                res = min(res, k)
                r = k - 1

        return res

