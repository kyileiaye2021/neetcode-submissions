class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # happy cases
        # input: ["pot", 'top', 'horse']
        # output: [["pot", "top"], ['horse']]

        # input: ["x", 'y']
        # output: [['x'], ['y']]

        # input: ['key', 'ke']
        # output: [['key'], ['ke']]

        # edge cases
        # input: ['x']
        # output: [['x']]

        # input: ['']
        # output: [['']]

        # input: []
        # output: []

        # hashmap 
        # {{a:1, c:1, t:1}: ["act", "cat"]}
        # {a:1, c:1, t:1} not the same {c:1, a:1, t: 1}
        # [0, 0, 0, ..., 0]
        # abc -> [1,1,1,...,0]
        # cab -> [1,1,1,...,0]
        # a = 0, b = 1, c = 2, ...
        # a = 97 = ord(a)
        # index = ord(a) - 97
        # {(1,1,1,...,0): ["act", "cat"]}

        # hashmap
        # iterate thru the s in strs
        #   create a list of 26 zeros 
        #   iterate thru the char in s
        #       increment 0 at the corresponding position by 1
        #   convert that list to tuple
        #   check if the tuple is already in the hashmap
        #       add the s to the list of corresponding tuple
        #   else
        #       add the tuple with the list with the s 
        # iterate thur the hashmap values 
        #   return the list of the groups 

        hashmap = defaultdict(list)

        for s in strs:
            temp_lst = [0] * 26
            for c in s:
                index = ord(c) - 97
                temp_lst[index] += 1

            temp_tuple = tuple(temp_lst)

            if temp_tuple in hashmap:
                hashmap[temp_tuple].append(s)

            else:
                hashmap[temp_tuple] = [s]

        
        res_lst = [group for group in hashmap.values()]
        return res_lst



