class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def isPalindrome(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False

                i += 1
                j -= 1
            return True

        def recur(i):
            # base case
            if i >= len(s):
                res.append(part.copy())
                return

            # recursive case
            for j in range(i, len(s)):
                if isPalindrome(s, i, j):
                    part.append(s[i: j + 1])
                    recur(j + 1)
                    part.pop()

            
        recur(0)
        return res