class Solution:
    def isPalindrome(self, s: str) -> bool:
        # happy case
        # s = "ab c ba"
        # output = true

        # s = "Aba"
        # output = true

        # s = 'abc'
        # output = false

        # edge case
        # s = 'a'
        # output = true

        # forward backward two pointers
        # iterate until l passes r
        #   check if l ele is non-alphanumeric char
        #       l += 1
        #   check if r elel is non-alphanumeric char
        #       r -= 1
        #   if l or r ele is upper case, convert it lower case
        #   check if l and r ele are the same
        #       l += 1
        #       r -= 1
        #   else: return false

        l, r = 0, len(s) - 1

        while l <= r:

            if not s[l].isalnum():
                l += 1
                continue

            if not s[r].isalnum():
                r -= 1
                continue

            if s[l].lower() != s[r].lower():
                return False

            else:
                l += 1
                r -= 1

        return True
        