class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # create a dict {char: freq count}
        # iterate  over s
        #   check if the curr char is in the dict
        #       check if the freq count is greater than 0
        #           decrement that freq count
        #       else: return false
        #   else: return false
        # return true

        # Time: O(n)
        # Space: O(n)

        if len(s) != len(t):
            return False

        map = {}

        for ele in s:
            if ele not in map:
                map[ele] = 1
            else:
                map[ele] += 1
            
        for ele in t:
            if ele in map:
                if map[ele] > 0:
                    map[ele] -= 1
                else:
                    return False
            
            else:
                return False

        return True
