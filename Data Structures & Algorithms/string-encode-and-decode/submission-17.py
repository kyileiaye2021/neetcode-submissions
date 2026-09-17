class Solution:

    def encode(self, strs: List[str]) -> str:

        # ["h", 'L']
        # hL
        # 1#h1#L

        # [" n", "#y"]
        # '2 n2#y'

        # ''
        # ''

        res_str = ''
        for s in strs:
            res_str += str(len(s)) + "#" + s

        return res_str

    def decode(self, s: str) -> List[str]:

        # 1#h1#L
        # ["h", 'L']

        # ' n#y'
        # [" n", "#y"]

        # ''
        # ['']

        if s == '':
            return []

        res_lst = []
        i = 0
        j = 0

        while j < len(s):

            while s[j] != '#':
                j += 1
            print(i)
            print(j)
            count = int(s[i:j])
            i = j + 1
            j = i + count
            res_lst.append(s[i:j])
            i = j
        return res_lst
            





