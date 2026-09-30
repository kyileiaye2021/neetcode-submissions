class Solution:
    def climbStairs(self, n: int) -> int:
        # starting from n, at each recursive step, we are doing 1 step or 2 step
        # recur_func(n)
        #   base case
        #   if n == 0:
        #       return 1
        #   if n < 0:
        #       return 0
        #   recursive case
        #   if arr[n] > 0:
        #       return arr[n]
        #   one_step = recur_func(n-1) # taking 1 step
        #.  two_step = recur_func(n - 2) # taking 2 step
        #   arr[n] = one_step + two_step

        arr = [0] * (n + 1)

        def recur_func(n):
            # base case
            if n == 0:
                return 1

            if n < 0:
                return 0

            # recursive case
            if arr[n] > 0:
                return arr[n]

            one_step = recur_func(n - 1)
            two_step = recur_func(n - 2)

            arr[n] = one_step + two_step

            return arr[n]

        return recur_func(n)
    