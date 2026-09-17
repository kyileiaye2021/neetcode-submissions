class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # we use brute force -> recursion

        # res len = 0
        # res substr = ""
        # start from the ele and expand the l, r pointer
        # iterate thru the ele
        #   l, r 
        #   check if l , r within the bounds. and  check if the l, r ele are the same
        #       if r - l + 1 > res len
        #           update the res substr
        #           update the res len
        # return res substr

        res_len = 0
        res_substr = ""

        for i, c in enumerate(s):

            # if the s is odd
            l, r = i, i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                curr_len = r - l + 1
                if curr_len > res_len:
                    res_substr = s[l: r + 1]
                    res_len = curr_len
                l -= 1
                r += 1

            # for even s
            l, r = i, i + 1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                curr_len = r - l + 1
                if curr_len > res_len:
                    res_substr = s[l: r + 1]
                    res_len = curr_len
                l -= 1
                r += 1

        return res_substr
