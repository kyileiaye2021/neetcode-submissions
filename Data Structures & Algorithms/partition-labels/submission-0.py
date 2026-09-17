class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        # hashmap {ele: last index}
        # size = 0
        # res list
        # iterate thru the ele
        #   get the last index for each ele and update max last index 
        #   increment the size 
        #   if curr index reach the max last index
        #       put size to res list
        #       reset size to 0
        # return res

        last_idx = {}
        for i, c in enumerate(s):
            last_idx[c] = i

        size = 0
        res_lst = []
        max_idx = 0

        for i in range(len(s)):
            cur_last_idx = last_idx[s[i]]
            max_idx = max(max_idx, cur_last_idx)
            size += 1
            
            if i == max_idx:
                res_lst.append(size)
                size = 0
                max_idx = i + 1

        return res_lst