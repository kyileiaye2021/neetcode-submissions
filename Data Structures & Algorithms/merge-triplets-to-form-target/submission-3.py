class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # input: [[1,2,3], [1,4,4], [5,3,2]], target = [5,4,4]
        # output: true

        # if there is only one list 
        #   if it is a target -> return true else return false

        # brute force - O(n^2)
        # iterate thru the triplets 
        #   iterate thru other triplets
        #       compare curr triplet and other triplet
        #           return true if it forms the target
        # return false

        # greedy ??
        # keep track of the max a, b, c each time we iterate thru the list
        # first max one is the first list
        # iterate thru the triplets
        #   update the max a,b,c
        # if max one == target, return true else false
        # if len(triplets) == 1:
        #     if triplets[0] == target:
        #         return True
        #     else:
        #         return False

        max_triplet = [float('-inf'), float('-inf'), float('-inf')]
        for i in range(len(triplets)):
            print(triplets[i])
            if triplets[i][0] > target[0] or triplets[i][1] > target[1] or triplets[i][2] > target[2]:
                continue
            max_triplet = [max(max_triplet[0], triplets[i][0]), max(max_triplet[1], triplets[i][1]), max(max_triplet[2], triplets[i][2])]
            print(max_triplet)

        return True if max_triplet == target else False


        