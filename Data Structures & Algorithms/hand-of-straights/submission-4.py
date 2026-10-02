class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # hashmap
        # minheap
        # starting from the first ele in min heap
        #   try to find each element in the group a
        #   if it's in the hashmap ,
        #       decement the count
        #   else; return false
        #   if the count == 0
        #       if the first ele != the curr i
        #           return false
        #       pop that ele
        # return true

        if len(hand) % groupSize:
            return False

        count = {}
        for h in hand:
            count[h] = 1 + count.get(h, 0)

        minH = list(count.keys())
        heapq.heapify(minH)

        while minH:
            first = minH[0]
            for i in range(first, first + groupSize):
                if i not in count:
                    return False

                count[i] -= 1

                if count[i] == 0:
                    if minH[0] != i:
                        return False

                    heapq.heappop(minH)

        return True
