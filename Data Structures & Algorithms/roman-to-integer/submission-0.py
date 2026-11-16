class Solution:
    def romanToInt(self, s: str) -> int:
        # IV - 4
        # VI - 6
        # LI - 51
        # XL - 40

        # if the curr char is > prev char
        #   subtract the prev from the curr

        # iterate thru the char
        #   get the corresponding pair for that char
        #   if the char is second char
        #       check if the curr > the prev one
        #           subtract the prev one
        #   add the curr char

        r_to_int = {'I': 1, 'V': 5, 'X':10, 'L':50, 'C':100, 'D':500, 'M': 1000}

        total = 0

        for i, c in enumerate(s):
            num = r_to_int[c]
            if i > 0:
                prev_num = r_to_int[s[i - 1]]
                if num > prev_num:
                    total -= prev_num
                    num = num - prev_num

            total += num

        return total


