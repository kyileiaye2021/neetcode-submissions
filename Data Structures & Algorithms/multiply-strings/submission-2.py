class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # happy case
        # nums1 = "3", nums2 = "4"
        # output: "12"

        # nums1 = "111", nums2 = "222"
        # output: "24642"

        # edge cases
        # nums1 = "0", nums2 = "1"
        # output: "0"

        # nums2 = "0", nums2 = "0"
        # output: "0"

        # set larger str to num1 and smaller ster to num2
        # create a res lst of size (m + n) initialized to 0
        # reverse the two input str and convert them to list
        # num2 - smaller str, num1 = larger str

        # iterate thru the ele in num2 (i)
        #   iterate thru the ele in num1 (j)
        #       multiply ith num2 and jth num1
        #       res[i] = res[i] + product % 10
        #       res[i + 1] = product // 10
        # reverse the list
        # join it and return
        if num1 == '0' or num2 == '0':
            return '0'
        num1 = num1.split(',')
        num2 = num2.split(',')
        n = num1[::-1]
        m = num2[::-1]

        if len(num1) > len(num2):
            n = num2
            m = num1

        else:
            n = num1
            m = num2
        
        print(n)
        print(m)
        res = [0] * (len(num1) + len(num2))

        for i in range(len(n)):
            for j in range(len(m)):
                multiply = (int(n[i]) * int(m[j]))
                print(multiply)

                temp_res = multiply % 10
                carry = multiply // 10

                res[i] = res[i] + temp_res
                res[i + 1] = carry

        res = res[::-1] # reverse the list
        i = 0
        # removing leading zeros
        while i < len(res) and res[i] == 0:
            i += 1

        res = res[i : ]
        # converting the int back to str
        for j,k in enumerate(res):
            res[j] = str(k)

        return ''.join(res)


