class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # two pointers
        # create a hashmap
        # while r < len(s)
        #   add the freq in the hashmap
        #   curr window size - most freq > k
        #       shrink the window size
        #   max_window size
        freq_map = {}
        l, r = 0, 0
        max_window = 0

        while r < len(s):
            freq_map[s[r]] = 1 + freq_map.get(s[r], 0)

            while (r - l + 1) - max(freq_map.values()) > k:
                freq_map[s[l]] -= 1
                l += 1

            max_window = max((r - l + 1), max_window)
            r += 1

        return max_window
