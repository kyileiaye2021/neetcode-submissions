class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # 10
        # [25, 64, 9, 4, 10]
        # 8
        # [25, 8, 9, 4, 10]
        # 5
        # [5, 8, 9, 4, 10]
        # [5, 8, 9, 4, 3] = 29

        gifts = [-g for g in gifts]
        heapq.heapify(gifts)

        while k > 0:
            ele = floor(sqrt(-heapq.heappop(gifts)))
            heapq.heappush(gifts, -ele)
            k -= 1
        
        gifts = [-g for g in gifts]
        return sum(gifts)


