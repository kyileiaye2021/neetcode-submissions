class Solution:
    def total_helper(self, n):
        total = 0
        while n != 0:
            rem = n % 10
            n = n // 10
            total += rem**2
            print('Inside loopp', total)

        print('Total', total)
        return total

    def isHappy(self, n: int) -> bool:
        # duplicate set to store the res at each step
        # while n != 1 or n is no in that set
        #   get the total of each n
        #   put it to the set

        if n == 1:
            return True
        
        duplicates = set()
        while n != 1 and n not in duplicates:
            duplicates.add(n)
            n = self.total_helper(n)
            if n == 1:
                return True

        return False