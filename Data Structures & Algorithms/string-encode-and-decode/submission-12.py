class Solution:
    # ['Hello', 'World']
    # '#5Hello#5World'

    # if curr char == #
    #    retrieve num of chars
    #    retrieve the curr word substr
    #    append the curr word back to lst

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)) + '#' + s) # ['5#Hello', '#5World']

        return ''.join(res) # '#5Hello#5World'

    def decode(self, s: str) -> List[str]:

        i = 0
        res = []
        while i < len(s):
            j = i # represent num of chars
            while s[j] != '#':
                j += 1
            num_of_chars = int(s[i : j])
    
            
            i = j + 1
            curr_word = s[i : i + num_of_chars]
            print(curr_word)
            res.append(curr_word)
            i += num_of_chars
        
        return res

