class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # t map
        # need = count of unique ele in tmap
        # have = 0
        # s map
        # i, j = 0, 0
        # min_window = 0
    
        # itereate thru s
        #   check if curr s ele in t map
        #       add curr s ele in the s map
        #       if curr s ele in t map == smap[curr s ele]
        #           have += 1
        #       While need == have
        #           curr window = r - l + 1
        #           update min window
        #           if i ele in s map
        #               decrement the s map[i ele]
        #               have -= 1
        #           i += 1
        #   j += 1  

        # return min window

        tmap = Counter(t)
        need = len(tmap)
        have = 0
        smap = {}
        min_window_size = float('inf')
        min_window = ''
        i, j = 0, 0

        while j < len(s):
            if s[j] in tmap:
                smap[s[j]] = 1 + smap.get(s[j], 0)
                if smap[s[j]] == tmap[s[j]]:
                    have += 1

                while have == need:
                    curr_window_size = j - i + 1
                    if curr_window_size < min_window_size:
                        min_window = s[i: j + 1]
                        min_window_size = curr_window_size

                    if s[i] in smap:
                        smap[s[i]] -= 1
                        if smap[s[i]] < tmap[s[i]]:
                            have -= 1
                    
                    i += 1

            j += 1

        return min_window

