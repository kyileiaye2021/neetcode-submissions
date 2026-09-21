class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # hashmap for s1
        # hashmap for s2
        # add 3 ele in side s2 map
        # and check matches
        # itearete thru s2 from j 
        #   add curr to s2 map
        #   if curr ele in s1 map
        #       if s1map ele != s2 map ele
        #           decrement matches by 1
        #   else: decrement matches by 1
        #   if matches == 26, return true
        #   decrement l ele in s2 map
        #   if l ele not in s1 map, increment matches by 1
        #   return false

        if len(s1) > len(s2):
            return False
        s1_arr = [0] * 26
        s2_arr = [0] * 26

        for i in range(len(s1)):
            s1_arr[ord(s1[i]) - ord('a')] += 1
            s2_arr[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            if s1_arr[i] == s2_arr[i]:
                matches += 1

        j = 0
        for i in range(len(s1), len(s2)):
            if matches == 26:
                return True

            idx = ord(s2[i]) - ord('a')
            s2_arr[idx] +=1
            if s2_arr[idx] == s1_arr[idx]:
                matches += 1

            elif s1_arr[idx] + 1 == s2_arr[idx]:
                matches -= 1

            idx = ord(s2[j]) - ord('a')
            s2_arr[idx] -= 1
            if s2_arr[idx] == s1_arr[idx]:
                matches += 1

            elif s1_arr[idx] - 1 == s2_arr[idx]:
                matches -= 1
            j += 1
            

        return False if matches != 26 else True