class Solution:
    
    def encode(self, strs: List[str]) -> str:

        res_str = ""
        for s in strs:
            res_str += str(len(s)) + '#' + s

        return res_str

    def decode(self, strs: List[str]) -> List[str]:

        res = []
        i = 0
        j = 0
        while j < len(strs):

            while strs[j] != '#':
                j += 1

            length = int(strs[i:j]) # count of the str

            i = j + 1
            j = i + length
            temp_str = strs[i:j]
            res.append(temp_str)

            i = j
        return res