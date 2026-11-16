class Solution:
    def intToRoman(self, num: int) -> str:
        # subtract the largest ith num smaller than num
        # 1994
        # 1994 - 1000 = 994 --> M
        # 994 - 900 = 94 --> MCM
        # 94 - 90 --> MCMXC
        # 4 --> MCMXCIV

        # 3749
        # 3749 - 3000 = 749 --> MMM
        # 749 - 700 = 749 - (700 - 500) = 749 - (500 + 100 + 100) = 49 --> MMMDCC
        # 49 - 40 = MMMDCCXL
        # 9 ==> MMMDCCXLIX

        # 4

        # list - [1000, 500, ... 1]
        # hashmap : {1000: M, 500: D, ...}
        # iterate thru the list
        #   try to divide the curr num by list ith num
        #        if the division is >= 1:
        #           count = 
        #           multiply the curr roman char with that count
        #           add it to res
        #       else
        #           go to next char
        # return res

        lst = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        int_to_r = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
                    100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X',
                    9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}

        res = ''
        for i in lst:
            if num // i:
                count = num // i
                res += (int_to_r[i] * count)
                num = num % i

        return res



