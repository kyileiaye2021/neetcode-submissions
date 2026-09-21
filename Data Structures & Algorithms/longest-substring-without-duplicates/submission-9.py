class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # 2 poiner sliding window
        # max window = 0
        # set 
        # i, j = 0, 0
        # while j < len(s)
        #   check if j ele in set
        #       remove i ele from the set
        #       i += 1
        #   
        #   add j ele to the set
        #   j += 1
        #   find the window size (j - i)
        #   update max window
        # return max window

        max_window = 0
        visited = set()
        i, j = 0, 0

        while j < len(s):
            while s[j] in visited:
                visited.remove(s[i])
                i += 1

            visited.add(s[j])
            j += 1

            curr_window = j - i
            max_window = max(max_window, curr_window)

        return max_window
