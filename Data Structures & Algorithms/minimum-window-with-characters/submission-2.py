class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # happy case
        # s = "xyhthztheaxvyzte", t = "xyz"
        # output: "xvyz"

        # s = "xyxz", t = "xyz"
        # output: "xyxz"
        
        # edge cases
        # s = "x", t = "xy"
        # output: ""

        # s = "x", t = "l"
        # output: ""

        # if len of s < len(t) --> return empty str
        # change the t to set 
        # iterate thru the str
        #   move both l and r if the curr ele is not in the set
        #   while r doesn;t still hit the end
        #       check if curr r is in the set
        #           count += 1
        #       increment r
        #       if count == len(set)
        #           reset count = 0
        #           move l to r
        #           break

        # res_lst = []
        # if len(s) < len(t):
        #     return ""

        # t_set = set(t)
        # max_count = 0
        # l, r = 0, 0
        # while r < len(s):
        #     while r < len(s) and s[r] not in t_set:
        #         l += 1
        #         r += 1

        #     t_count = 0
        #     res = ""
        #     while r < len(s):
        #         if s[r] in t_set:
        #             t_count += 1

        #         res += s[r]
        #         r += 1
        #         if t_count == len(t_set):
        #             res_lst.append(res)

        #         while t_count >= len(t_set):
        #             if s[l] in t_set:
        #                 t_count -= 1
        #             l += 1



        # min_substr = float('inf')
        # min_substr_idx = 0
        # for i, ele in enumerate(res_lst):
        #     if len(ele) < min_substr:
        #         min_substr = len(ele)
        #         min_substr_idx = i
        # return res_lst[min_substr_idx]

        if t == "":
            return ""
        window = {}
        count_t = {}
        l = 0
        
        for c in t:
            count_t[c] = count_t.get(c, 0) + 1
        
        have = 0
        need = len(count_t)
        res = [-1, -1]
        res_len = float('inf')

        for r in range(len(s)):

            # go upto where all elements in the t are included in s
            window[s[r]] = window.get(s[r], 0) + 1 # window dict is for all ele
            if s[r] in count_t and window[s[r]] == count_t[s[r]]:
                have += 1 # update the num of ele met in s

            while have == need: 
                # update the result
                if r - l + 1 < res_len:
                    res = [l, r]
                    res_len = r - l + 1
                
                # shrinking the window size
                window[s[l]] -= 1
                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l : r + 1] if res_len != float('inf') else ""



            