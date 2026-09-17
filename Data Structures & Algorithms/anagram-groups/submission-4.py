class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # happy cases
        # strs = ["act", "ca", "cat"]
        # output: [["act", "cat"], ["ca"]]
        
        # edgecases
        # strs = ["act", "ga"]
        # output: [["act"], ["ga"]]

        # strs = ["", "ga"]
        # output: [[""], ["ga"]]

        # strs = [""]
        # output: [[""]]

        # create a dict for the 1st word
        # group_dict = {dict: [words]}

        # iterate thru the ele 
        #   create the temp arr of length 26 with 0 value
        #   iterate thru the chars
        #       ASCII value of the curr char
        #       index = subtract 65 from that curr char
        #       increment the value at that index in temp arr
        #       join every ele in temp arr and convert to str

        #   
        #   check if the temp str is in group dict
        #       append the curr word to the curr temp str
        #   else
        #       add the current str with its correspoiinding word to group dict

        # res list
        # iterate group dict values
        #   add the curr val to res list

        # return res list

        group_dict = {}

        for word in strs:
            temp_arr = [0] * 26

            for c in word:
                cur_val = ord(c)
                cur_index = cur_val - 97
                temp_arr[cur_index] += 1

            cur_str = tuple(temp_arr)
                
            if cur_str in group_dict:
                group_dict[cur_str].append(word)

            else:
                group_dict[cur_str] = [word]

        
        res = []
        for val in group_dict.values():
            res.append(val)

        return res


                

