class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # get the size of the s1
        # l, r
        # 0, r = s1 + l
        # create a freq map for the s1
        # until r reaches to the end
        #   make a freq map for that curr window
        #   check if the freq map of s1 and freq map of curr window are the same
        #       return True
        # return False

        s1_freq = {}
        for ele in s1:
            s1_freq[ele] = 1 + s1_freq.get(ele, 0)

        size = len(s1)
        l = 0
        r = 0
        window = Counter()

        while r < len(s2):
            count = 0
            window[s2[r]] += 1

            if (r - l + 1) > len(s1):
                window[s2[l]] -= 1
                if window[s2[l]] == 0:
                    del window[s2[l]]

                l += 1

            # curr_window_map = {}
            # for i in range(l, r + 1):
            #     curr_window_map[s2[i]] = 1 + curr_window_map.get(s2[i], 0)

            if s1_freq == window:
                return True

            r += 1

        return False

