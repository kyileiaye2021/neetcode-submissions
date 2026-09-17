class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # input: s = "zxyzxyx"
        # output: 3

        # input: s = "xxxyz"
        # output: 3

        # input: s = ""
        # output: 0

        # input: s = "xyzcdb"
        # output: 6
        
        # input: s = "zybxzuab"
        # output: 6

        # brute force - O(n^2)
        # sliding window - O(n)

        # l, r = 0, 0
        # longest = 0
        # iterate thru the s until r reaches the end
        #   while the curr char is in visited
        #       remove the curr left pointer ele from the visited
        #       move the left pointer
        #   add the curr char to visited
        #   curr_window= r - l + 1
        #   r += 1
        #   longest = max(longest, curr_window)
        # return longest

        l = r = 0
        visited = set()
        longest = 0

        while r < len(s):
            while s[r] in visited:
                visited.remove(s[l])
                l += 1
            
            visited.add(s[r])
            curr_window = r - l + 1
            r += 1
            longest = max(longest, curr_window)
        return longest
