class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        start_time_heap = []

        for i, (start, process) in enumerate(tasks):
            heapq.heappush(start_time_heap, (start, process,i))
        
        print(start_time_heap)

        time = start_time_heap[0][0]
        res = []
        order_heap = []

        while order_heap or start_time_heap:
            
            while start_time_heap and start_time_heap[0][0] <= time:
                start, process, i = heapq.heappop(start_time_heap)
                heapq.heappush(order_heap, (process, i))

            if order_heap:
                process, i = heapq.heappop(order_heap)
                time += process
                res.append(i)

            else: # instantly start a new task if there is no task in the order heap
                time = start_time_heap[0][0]
        return res


        