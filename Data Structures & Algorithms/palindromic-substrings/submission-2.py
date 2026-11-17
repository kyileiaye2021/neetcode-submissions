class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        for i in range(len(s)):
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # curr_window_len = r - l + 1
                # if longest < curr_window_len:
                #     longest = curr_window_len
                #     res_window = s[l:r + 1]
                count += 1
                l -= 1
                r += 1

        return count
