class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # happy case
        # s = "zxyzxy"
        # output: 3

        # s = "yyyyxu"
        # output: 3

        # s = "utyyerx"
        # output: 4

        # edge cases
        # s = "xxxx"
        # output: 1

        # s = "abcxeg"
        # output: 6

        # set
        # max window = 0
        # iterate thru the list
        #   check while the curr ele in set
        #       increment the left 
        #       remove the ele from the set
        #   else
        #       add the ele to the set
        #       increment the right 
        #   find the curr window size
        #   update the max window size

        max_window = 0
        left, right = 0,0
        unique = set()

        while right < len(s):
            if s[right] in unique:
                while s[right] in unique:
                    unique.remove(s[left])
                    left += 1

            else:
                unique.add(s[right])
                right += 1
                curr_window = (right - left)
            max_window = max(max_window, curr_window)

        return max_window
            

