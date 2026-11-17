class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # hashmap
        # {{'c':2, 'a':1}: [acc, cac, cca]}
        # 0 --> a, 1 --> b, 2 --> c,
        # map = {[1,0,1,0,0..]: [acc,cac, cca]}

        # itereate thru the map
        #   append the list to the res list

        # return res

        map = {}

        for s in strs:
            curr_lst = [0] * 26
            for c in s:
                curr_lst[ord(c) - ord('a')] += 1

            curr_lst = tuple(curr_lst)
            if curr_lst not in map:
                map[curr_lst] = [s]

            else:
                map[curr_lst].append(s)
        
        res = []
        for group in map.values():
            res.append(group)

        return res

