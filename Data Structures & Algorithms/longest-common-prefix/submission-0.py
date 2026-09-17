class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # input: strs = [,"bbag", bbat"","bbank","bband"]
        # output: "bba"

        # input: strs = ["dance", "dag", "damage"]
        # output: "da"

        # input: strs = ["banana", "dag"]
        # output: ""

        # input: strs = ["1$21", "gag"]
        # output: ""

        # input: strs = ["neet", "eetn"]
        # output: ""

        # input: strs = ["helle", "helle"]
        # output: "helle"

        # input: strs = []
        # output: ""

        # hashmap for each str (need to consider for order so may not probably work)
        # sliding window

        # create a hashmap for the first ele
        # iterate thru the ele
        #   iterate thru the char for each str
        
        prefix = strs[0]

        for s in strs:
            res = ""
            for i in range(min(len(s), len(prefix))):

                if s[i] != prefix[i]:
                    break

                res += s[i]
            prefix = res

        return prefix
                

