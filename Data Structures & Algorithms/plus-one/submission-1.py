class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        # convert each int to str and combine the ele and convert back to int
        # add 1 to int and convert back to str
        # split the ele and convert each ele to int

        # O(n) time and O(n) space

        # digits = [str(digits[i]) for i in range(len(digits))] # ['1','2','3','4']
        # digits = ''.join(digits) # '1234'
        # digits = int(digits) + 1 # convert to int and add 1
        # digits = list(str(digits)) # convert back to str and split
        # digits = [int(digits[i]) for i in range(len(digits))] # convert each ele to int 
        # return digits

        
        res = 0
        for i in range(len(digits)):
            res = (res * 10) + digits[i]

        res += 1
        
        res_lst = []
        while res != 0:
            rem = res % 10
            res = res // 10
            res_lst.append(rem)
        
        return res_lst[::-1]

        


