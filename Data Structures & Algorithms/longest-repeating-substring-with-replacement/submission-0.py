class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Happy case
        # input: s = "AAB", k = 1
        # output: 3

        # Edge case
        # input: s = "A", k =1
        # output = 1

        # input: s = "BAA", k = 1
        # output = 3

        # Brute Force Approach - use nested loop and keep track of the longest val 
        # Sliding Window Approach with variable size

        # create a dict to store the unique chars and their freq
        # l, r both pointing to 0s
        # longest to keep track of longest length of substr
        # iterate until the r reaches the end of the list
        #   update the freq count of the curr char
        #   curr window size = (r - l +1)
        #   check if the curr window size - most freq num of char in the dict is greater than k
        #       while curr window size - most freq num of char in the dict is greater than k
        #           decrement the freq count of the l pointer char
        #           increment l by 1
        #   update the longest with the max between the longest and the curr window size 
        # return longest

        # AABAABBA
        curr_chars = {}
        l = 0
        longest = 0

        for r in range(len(s)):
            curr_chars[s[r]] = 1 + curr_chars.get(s[r], 0)

            most_freq = max(curr_chars.values())
            if (r - l + 1) - most_freq > k:
                curr_chars[s[l]] -= 1
                l += 1

            longest = max(longest, (r - l + 1))

        return longest
