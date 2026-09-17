class Solution:
    def reverse(self, x: int) -> int:

        # res = ''
        # until x is 0
        #   divide x by 10
        #   y = mod x by 10
        #   convert y to str add it to the res
        # return res
        temp = x

        if x < 0:
            temp = x * -1

        print(temp)

        res = ""
        while temp != 0:
            y = temp % 10
            temp = temp //10
            res += str(y)
        
        res = int(res) if res else 0
        if x < 0:
            res = res * -1 
        
        print("After loop", res)
        return res if res <= 2**31 and res >= -2**31  else 0
