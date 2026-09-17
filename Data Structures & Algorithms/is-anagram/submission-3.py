class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # hashmap
        # if s and t len not the same return false

        # convert s to hashmap {r:1, a:1, c:1, e:1}
        # convert t to hashmap {c:1, e:1, a:1, r:1}
        # O(n) time
        # O(n) space

        if len(s) != len(t):
            return False

        s_hash = Counter(s)
        t_hash = Counter(t)

        for k, v in s_hash.items():
            if k not in t_hash or v != t_hash[k]:
                return False

        return True


        