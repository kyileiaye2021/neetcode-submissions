class Solution:
    def reverse(self, x: int) -> int:

        # res = ''
        # until x is 0
        #   divide x by 10
        #   y = mod x by 10
        #   convert y to str add it to the res
        # return res
        # temp = x

        # if x < 0: # change neg val to pos to operate on the digits
        #     temp = x * -1

        # res = ""
        # while temp != 0:
        #     y = temp % 10
        #     temp = temp //10
        #     res += str(y)
        
        # res = int(res) if res else 0 # if just 0, return 0

        # # if neg, change it back to neg
        # if x < 0:
        #     res = res * -1 
        
        # return res if res <= 2**31 and res >= -2**31  else 0


        temp = x

        if x < 0: # change neg val to pos to operate on the digits
            temp = x * -1

        res = 0
        while temp != 0:
            y = temp % 10
            temp = temp //10
            res = (res * 10) + y

        # if neg, change it back to neg
        if x < 0:
            res = res * -1 
        
        return res if res <= 2**31 and res >= -2**31  else 0

