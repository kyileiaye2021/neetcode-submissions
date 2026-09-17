class Solution:

    # the input is a list of str and the output is also a list of str
    # combine each str as a str
    # separate them out back to an orig list

    # happy cases
    # input - ["I", "U"]
    # str = "IU"
    # output - ["I", "U"]

    # edge cases
    # input - []
    # output - []

    # input - ["I", "", "U"]
    # output - ["I", "", "U"]
    

    def encode(self, strs: List[str]) -> str:
        # str - "1#I1#U"
        # create an empty str
        # iterate thru the list
        #   get the len of curr str
        #   concatenate the str with the len, curr str, #

        combined_str = ""
        for word in strs:
            curr_word_len = len(word)
            combined_str += str(curr_word_len) + "#" + word

        return combined_str

    def decode(self, s: str) -> List[str]:
        # str - "1I1U"

        res = []
        i = 0
        while i < len(s):
            j = i # j will point to the #

            while s[j] != '#':
                j += 1

            curr_word_len = int(s[i:j]) # extracting the len of word
            res.append(s[j+1 : j+1+curr_word_len]) # from the pos after # to the end of the word
            i = j + 1 + curr_word_len

        return res



