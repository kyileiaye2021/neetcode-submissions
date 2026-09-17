class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # l , r
        #    create a set for each window
        # max window = 0

        # iterate thru the chars
        #    if curr ele not in set
        #       add it to the set
        #       move r by 1
        #   else
        #       get the curr window size and update max window size
        #       while curr in set
        #           move the l pointer
        #           remove l ele in the set
        # return max window

        l,r = 0, 0
        unique = set()
        max_window = 0

        while r < len(s):
            if s[r] not in unique:
                unique.add(s[r])
                r += 1
                curr_window = r - l 

            else:

                while s[r] in unique:
                    unique.remove(s[l])
                    l += 1

            max_window = max(max_window, curr_window)

        return max_window