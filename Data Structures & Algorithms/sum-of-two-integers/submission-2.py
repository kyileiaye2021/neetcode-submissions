class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF
        
        res = a
        carry = b
        
        while carry != 0:
            new_carry = ((res & carry) << 1) & mask
            res = (res ^ carry) & mask
            carry = new_carry

        return res if res <= max_int else ~(res ^ mask)