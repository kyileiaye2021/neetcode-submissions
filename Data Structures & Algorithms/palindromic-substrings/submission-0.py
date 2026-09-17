class Solution:
    def countSubstrings(self, s: str) -> int:
        
        # res set to store the substr
        # iterate thru the ele 
        #   l, r  - will start pointing to the i 
        #   whiile l and r within the bound and they are equal
        #       curr substr
        #       add the curr substr to the res set

        #   l = i, r = i + 1
        #   whiile l and r within the bound and they are equal
        #       curr substr
        #       add the curr substr to the res set

        # return the res set

        res = []

        for i in range(len(s)):
            # odd len
            l, r = i, i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                curr_substr = s[l:r+1]
                res.append(curr_substr)
                l -= 1
                r += 1

            # even len
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                curr_substr = s[l:r+1]
                res.append(curr_substr)
                l -= 1
                r += 1

        return len(res)
