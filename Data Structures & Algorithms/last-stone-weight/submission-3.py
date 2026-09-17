import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # happy case
        # stones = [2,3,6,2,4]
        # output: 1

        # stones = [1, 2]
        # output: 1

        # stones = [1]
        # output: 1

        # edge cases
        # stones = [2,2]
        # output: 0

        # stones = [6,3,3]
        # output: 0

        # sort the arr
        # max heap??
        # until the len of arr is > 1
        #   operate on the largest 2 ele
        #       add a new ele with the updated one
        # return the ele in the list
        
        max_heap = [(-1 * n) for n in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            num1 = heapq.heappop(max_heap) * -1
            num2 = heapq.heappop(max_heap) * -1
            
            # print(f"{num1}")
            # print(f"{num2}")
            new_val = max(num1, num2) - min(num1, num2)
            new_val = new_val * -1
            # print(f"Added new val: {new_val}")

            heapq.heappush(max_heap, new_val)

        return -max_heap[0]


