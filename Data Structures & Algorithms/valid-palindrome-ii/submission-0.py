class Solution:
    def validPalindrome(self, s: str) -> bool:
        # two pointer

        l, r = 0, len(s) - 1
        skipped = False
        while l < r:

            if s[l].isalnum() and s[r].isalnum():

                if s[l].lower() != s[r].lower():

                    if not skipped:

                        if s[l].lower() == s[r-1].lower():
                            r -= 1
                        
                        else:
                            l += 1

                        skipped = True

                    else:
                        return False

                else:
                    l += 1
                    r -= 1

            elif not s[l].isalnum():
                l += 1

            elif not s[r].isalnum():
                r -=1

            else:
                l += 1
                r -= 1

        return True