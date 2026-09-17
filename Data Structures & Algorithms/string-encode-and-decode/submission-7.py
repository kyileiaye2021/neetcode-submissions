class Solution:

    def encode(self, strs: List[str]) -> str:

        res_str = ""

        for s in strs:

            res_str += str(len(s)) + "#" 
            res_str += s

        print(res_str)
        return res_str

    def decode(self, s: str) -> List[str]:
        
        res_lst = []
        i = 0
        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])

            i = j + 1
            j = i + length
            curr_str = s[i:j]
            res_lst.append(curr_str)
            i = j 
            
        return res_lst