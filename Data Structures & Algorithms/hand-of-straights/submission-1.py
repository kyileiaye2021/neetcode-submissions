class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # if len(hand) % groupSize != 0:
        #     return False

        # hand.sort()
        # count = Counter(hand)

        # for h in hand:
        #     if count[h]:

        #         for i in range(h, h + groupSize):

        #             if count[i] <= 0:
        #                 return False
        #             count[i] -= 1
        # return True

        if len(hand) % groupSize != 0:
            return False

        freq = Counter(hand)

        pq = list(freq.keys())
        heapq.heapify(pq)
        print(pq)

        while pq:
            first = pq[0]

            for h in range(first, first + groupSize):

                if h not in freq:
                    return False

                freq[h] -= 1
                if freq[h] == 0:
                    if h != pq[0]:
                        return False
                    heapq.heappop(pq)

        return True




        
        