class Solution:
    # happy case
    # ["Hello","World"]
    # output: ["Hello","World"]

    # edge case
    # ["Hello#","World"]
    # output: ["Hello#","World"]

    # ["u", "##"]
    # output: ["###*#", "##"]

    def encode(self, strs: List[str]) -> str:

        # use the special chars with len of words 
        # total : "#3___#2__"
        res = ""
        for word in strs:
            res += str(len(word)) + "#" + word
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        
        # if the char is #
        # look at the num beside #
        # iterate thru that num of times
        #   create a word
        # add the word to res

        i = 0
        res = []

        while i < len(s):

            j = i
            while s[i] != "#":
                i += 1

            word_count = int(s[j : i])
            j = i + 1
            curr_word = s[j :  j + word_count]

            res.append(curr_word)

            i = j + word_count

        return res

