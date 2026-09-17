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

        last_index_map = {}
        res = []
        for i,c in enumerate(s):
            last_index_map[c] = i
        end = 0
        curr_size = 0

        # iterate thru the char
        #   get the last index 
        #   update the end of curr substr if the last index is > end
        #   curr size += 1
        #   if curr_size == end
        #       add the curr size into res list
        #       reset curr size = 0
        #
        #   
        for i in range(len(s)):
            last_idx = last_index_map[s[i]]
            end = max(end, last_idx)
            curr_size += 1

            if i == end:
                res.append(curr_size)
                curr_size = 0
        return res

