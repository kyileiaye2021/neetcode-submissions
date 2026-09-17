class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # curr window size - most freq == k
        # if that is > k, we need to shrink the size of window by moving left pointer
        # we need to have most freq char so we may need hashmap to store the chars

        longest = 0
        l = 0
        r = 0
        freq_map = collections.defaultdict(int)

        while r < len(s):
            freq_map[s[r]] = freq_map.get(s[r], 0) + 1
            most_freq_val = max(freq_map.values())
            curr_window_size = r - l + 1

            if curr_window_size - most_freq_val > k:
                freq_map[s[l]] -= 1
                l += 1

            longest = max(longest, (r - l + 1))
            r += 1

        return longest