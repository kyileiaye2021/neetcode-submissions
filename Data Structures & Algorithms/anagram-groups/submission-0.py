class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # create a dictionary {[size 26 with default val to 0: a list of anagrams]}
        # iterate over each str in the list
        #   create a list of size 26 with default val to 0
        #   iterate over each char in the curr str
        #       update the list[curr char - 97] by incrementing by 1
        #   check if the curr list is in the dictionary
        #       append the curr str to the list corresponding to that list in the dictionary
        #   else: create a list with curr str 
        # create a res list
        # iterate over the values of dictionary
        #   append the list of anagrams to the res list
        # return the res list


        anagram_dict = {}

        for ele in strs:
            curr_list = [0] * 26 

            for char in ele:
                curr_list[ord(char) - 97] += 1

            curr_list = tuple(curr_list) # list cannot be a key of the dictionary so convert it to a tuple 
            if curr_list in anagram_dict:
                anagram_dict[curr_list].append(ele)
            
            else:
                anagram_dict[curr_list] = [ele]

        res = []
        for val in anagram_dict.values():
            res.append(val)

        return res