class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # input: strs = ["act","pots","tops","cat","stop","hat"]
        # Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

        # input: strs = ["act"]
        # ouput: [["act"]]

        # input: strs = [""]
        # output: [[""]]

        # hashmap
        # {hashmap: ["hat"]}

        map = {}
        res = []
        for curr_s in strs:
            curr_map = {}
             
            for char in curr_s:

                if char not in curr_map:
                    curr_map[char] = 0

                else:
                    curr_map[char] += 1

            curr_map = tuple(sorted(curr_map.items()))
            if curr_map not in map:
                map[curr_map] = [curr_s]
            
            else:
                map[curr_map].append(curr_s)

        for res_lsts in map.values():
            res.append(res_lsts)

        return res

                
            





