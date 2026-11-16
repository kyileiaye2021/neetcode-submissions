class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # hashmap
        # create a hashmap for each s and t
        # compare those 2 hashmap
        # O(m + n) time
        # O(m + n) space

        # O(m + n) time
        # O(m) space

        # O(m + n) time
        # O(n) space

        # s  = ""
        # t = "y"

        if len(s) != len(t):
            return False

        s_map = Counter(s)

        for char in t:
            if char not in s_map:
                return False

            if s_map[char] <= 0:
                return False

            s_map[char] -= 1

        return True
        