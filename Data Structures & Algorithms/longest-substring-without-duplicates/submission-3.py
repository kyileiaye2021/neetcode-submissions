class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # happy cases
        # input: s = "xyzz"
        # output: 3

        # input: s = "acbbcde"
        # output: 4

        # edge cases
        # input: s = "a"
        # output: 1

        # input: s = "abce"
        # output: 4

        # input: s = "aaaa"
        # output: 1

        # Sliding Window
        # set to store the visited elements 
        # queue to store the curr window elements
        # l,r 
        # until r reaches to the end
        #   check if r ele is already visited
        #       remove the elements in the set
        #       
        #   else
        #       add the curr char to set
        #       increment r by 1

        visited = set()
        l, r = 0, 0
        longest = 0
        counter = 0
        while r < len(s):

            if s[r] in visited:

                while s[r] in visited:
                    visited.remove(s[l])
                    counter -= 1
                    l += 1
            else:
                visited.add(s[r])
                counter += 1
                r += 1
                longest = max(longest, counter)

        return longest

        # Time: O(n)
        # Space: O(n)