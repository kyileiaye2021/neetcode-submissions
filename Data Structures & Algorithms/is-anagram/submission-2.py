class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # input: s = "car", t = "rac"
        # output: true

        # input: s = "racc", t = "rac"
        # output: false

        # input: s = 'a', t = 'b'
        # output: false

        # input: s = '', t = ''
        # output: true

        # hashmap
        if len(s) != len(t):
            return False

        s_map, t_map = {}, {}
        
        for char in s:
            if char not in s_map:
                s_map[char] = 0

            else:
                s_map[char] += 1

        for char in t:
            if char not in t_map:
                t_map[char] = 0

            else:
                t_map[char] += 1

        for key, values in s_map.items():
            if key in t_map:
                if s_map[key] != t_map[key]:
                    return False

            else:
                return False

        return True


    # time complexity - O(n)
    # space complexity - O(n)
        