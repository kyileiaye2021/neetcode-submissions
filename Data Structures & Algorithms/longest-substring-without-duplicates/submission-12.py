class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # happy cases
        # zxyz = 3

        # ababab = 2
        
        # edge cases
        # aaaa = 1
        # abcd = 4
        # "" = 0

        # s = zxyzxyz
        # two pointers
        # sliding window
        # longest = 0
        # l = 0 
        # r = 0

        # while the curr ele is in the set
        #   remove the left ele from the set
        #   increment l
        #   
        # curr window len = r - l + 1
        # update longest if curr window len > longest
        # add curr ele to the set
        # increment r

        # return longest

        longest = 0
        l = 0
        r = 0
        seen = set()

        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1

            seen.add(s[r])
            curr_win_len = r - l + 1
            longest = max(longest, curr_win_len)
            r += 1

        return longest
        
