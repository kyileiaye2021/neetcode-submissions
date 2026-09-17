class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        hand.sort()
        freq_map = Counter(hand)

        for n in hand:
            
            if freq_map[n] > 0:
                for i in range(n, n + groupSize):
                    if freq_map[i] == 0:
                        return False

                    freq_map[i] -= 1

        return True
