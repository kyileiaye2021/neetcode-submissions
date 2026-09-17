class Solution:
    def countHelper(self, n):
        total = 0
        while n != 0:

            print("inside :", n)
            rem = n % 2
            n = n // 2
            print("inside rem :", rem)
            if rem == 1:
                total += 1
        print()

        return total

    def countBits(self, n: int) -> List[int]:
        
        # in one helper func
        # converting decimal to binary
        # total 
        # divide n by 2 each time until n becomes 0
        #   divide n by 2
        #   keep track of the rem
        #   increment total by 1 ifrem == 0
        # return total


        # res = []
        # while n >= 0:
        #   call helper func on n
        #   add the total count of each n to the res

        # return res

        res = [0] * (n + 1)

        while n >= 0:
            total = self.countHelper(n)
            res[n] = total
            n -= 1

        return res