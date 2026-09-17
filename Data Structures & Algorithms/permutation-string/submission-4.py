class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # input: s1 = "abc", s2 = "leacbg"
        # output: true

        # input: s1 = "abc", s2 = "leaacbag"
        # output: true

        # input: s1 = "b", s2 = "leabc"
        # output: true

        # input: s1 = "acvb", s2 = "elbvyac"
        # output: false

        # input: s1 = "", s2 = ""
        # output: true

        # input: s1 = "uu", s2 = ""
        # output: false

        # input: s1 = "", s2 = "hi"
        # output; true

        # sorting and two pointer searching  O(nlogn)
        # create a hashmap for s1
        # s1_count = count of s1
        # iterate thru the s2
        #   make a window of s1 count
        #   create a freq map for that window
        #   check if the curr map is == s1 map
        #       return true
        #   decrement freq count of l ele
        #   increment l by 1
        #   increment r by1 1
        # return false

        s1_count = len(s1)
        s1_map = Counter(s1)
        s2_map = {}
        i = 0
        while i < len(s2) - s1_count + 1:
            s2_map = Counter(s2[i : i + s1_count])
            print(s2_map)
            if s1_map == s2_map:
                return True

            s2_map[s2[i]] -= 1
            if s2_map[s2[i]] == 0:
                del s2_map[s2[i]]
            i += 1
        return False
