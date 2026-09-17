class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # s = "AAABABBBBB", k = 2
        # output: 7

        # s = "h", k = 5
        # output: 1

        # s = "h", k = 0
        # output: 1

        # hashmap/sliding window
        # iterate thru the ele until r reaches the end
        # add curr ele to hashmap
        # in each window
        #   find the most freq ele 
        #   while window size - most freq ele > k:
        #       decrement the count of l pointer ele
        #       increment l by 1
        #   update the longest window size
        #   increment r by 1
        # return longest window

        l = r = 0
        hashmap = {}
        longest = float('-inf')

        while r < len(s):
            hashmap[s[r]] = hashmap.get(s[r], 0) + 1

            while (r - l + 1) - max(hashmap.values()) > k:
                hashmap[s[l]] -= 1
                l += 1
            
            longest = max(r - l + 1, longest)
            r += 1

        return longest


