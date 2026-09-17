class Solution:
    def reverseBits(self, n: int) -> int:
        
        # new str
        # convert the n to the str
        # slice the last index of the n
        # add it to the new str
        # return the new str


        # convert to str
        # split the str to array
        # reverse the arr
        # combine 

        # 32 bits
        # reverse the binary rep
        # how can we get each bit at each position and replace it with corresponding reverse position
        
        # iterate thru each bit
        #   move each bit to the rightmost pos and extract with &
        #   move to the right to corresponding reverse pos and add it to res

        res = 0
        for i in range(32):
            bit = (n >> i) & 1 #extracting each bit 
            res += bit << (31 - i) # move to the right to corresponding reverse pos
        return res
        