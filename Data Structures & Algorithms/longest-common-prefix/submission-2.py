class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # if no str in the strs --> return ''
        # common hashmap = Counter(strs[0])
        # {b: 1, a:1}
        #  iterate thru the strs from second str
        #   curr hashmap = {}
        #    iterate thru the char
        #       if the char is in common hashmap
        #           add the char in the curr hashmap
        #    common hashmap = curr hashmap

        # return 

        # vertical search at index i for every str
        # ref str = strs[0]
        # iterate thru all ith indices for ref str
        #   iterate thru all strs
        #       if the curr ele is same as ref str at curr index
        #           add the curr ref char to the res
        # return res

        res = ""

        if len(strs) == 0:
            return res
        
        ref = strs[0]

        for i in range(len(ref)):
            for j in range(1, len(strs)):
                if i == len(strs[j]) or ref[i] != strs[j][i]:
                    return res
            res += ref[i]
        
        return res
        
        