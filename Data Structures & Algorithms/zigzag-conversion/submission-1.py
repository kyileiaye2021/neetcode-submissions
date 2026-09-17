class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # (numRows-1) * 2
        # 
        if len(s) <= 1:
            return s
        res = ''

        for i in range(numRows):
        
            for j in range(i, len(s), (numRows - 1) * 2):
                print(j)
                res += s[j]
                
                if i > 0 and i < numRows - 1 and (j + (((numRows - 1) * 2) - (2 * i))) < len(s):
                    res += s[j + (((numRows - 1) * 2) - (2 * i))]

        return res

