class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = 0
        res = ''
        for i in range(len(s)):
            
            # odd
            l = i
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

            curr_substr = s[l + 1: r]
            print(curr_substr)
            if len(curr_substr) > longest:
                res = curr_substr
                longest = len(res)

            # even
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

            curr_substr = s[l + 1: r]
            print(curr_substr)
            if len(curr_substr) > longest:
                res = curr_substr
                longest = len(res)

        return res                                     
 
        
       # abad
       # aba

       # abbbba
       # abbbba

       # abbdbb
       # bbdbb

       # abbc
       # bb

       # abba
       # 

           # longest

       # iterate thru the chars 
       #    for the odd len
       #    left = curr char, right = curr char
       #    go left and right
       #    check if l and r are not the same
       #        keep track of the curr str and the len only if the len is greater than the longest
       #    
       #    for the even len
       #    left. = curr char, right = right of the curr char
       #    go to the left and right
       #    check if l and r not the same 
       #        keep track of the curr str and the len only if the curr is greater than the longest

       # return longest substr

       
