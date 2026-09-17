class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # happy case
        # input: s1 = "abc", s2 = "abcd"
        # output: true

        # input: s1 = "abc", s2 = "baacd"
        # output: false

        # edge case
        # input: s1 = "abc", s2 = "cab"
        # output: true

        # input: s1 = "a", s2="a"
        # output: true
        
        # input: s1="ab", s2 = "cde"
        # output: false

        # Brute Force
        # Sliding Window 
    
        # l, r
        # k = size of s1
        # s1 dict
        # first check first k elements
        # make a dict to count freq of each char
        # check if they are the same as the s1 dict
        # return true if it is
        # iterate thru the list from second char
        #   make a dict to count the freq of each char in the curr window
        #   check if the curr window dict is the same as the s1 dict
        #       return true
        # return false

        l = 0
        if len(s1) > len(s2):
            return False
        
        s1_dict = Counter(s1)

        curr_window = Counter(s2[:len(s1)])
        if s1_dict == curr_window:
            return True

        for r in range(len(s1), len(s2)):
            curr_window[s2[r]] += 1 # include one more char
            curr_window[s2[l]] -= 1 # exclude the prev char
            if s1_dict == curr_window:
                return True
            l += 1
        
        return False



