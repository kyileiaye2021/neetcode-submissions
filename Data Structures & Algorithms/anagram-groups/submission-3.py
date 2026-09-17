class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # hashmap 
        # a code to represent each ele 
        # {(a-z)}: ele}

        # iterate thru the ele
        #   create a-z where the curr char is 1 and every other is 0
        #   add it to the hashmap with the ele
        
        # iterate thru the hashmap 
        #   create a new list
        #   iterate thru the list in each hashmap
        #       add the ele to the new list
        #   append the new list to the res list
        # return res list

        map = defaultdict(list)
        for s in strs:
            temp_hashcode = [0] * 26
            for c in s:
                curr_index = ord(c) - ord('a')
                temp_hashcode[curr_index] += 1

            map[tuple(temp_hashcode)].append(s)

        res_lst = []
        for temp_hashcode, ele_lst in map.items():
            temp_lst = []

            for ele in ele_lst:
                temp_lst.append(ele)
            
            res_lst.append(temp_lst)

        return res_lst


