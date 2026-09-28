class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # process the most freq char

        # count of chars in the tasks
        # add the count into max heap
        # while heap
        #   pop the most freq count
        #   time += 1
        #   task rem = freq count - 1
        #   if task rem != 0:
        #       queue.append(task rem, time + n)
        #   if time == first rem task's time
        #       pop the task rem from the queue and add it to the max heap
        # return time

        count_map = Counter(tasks)
        max_heap = [-cnt for cnt in count_map.values()]
        heapq.heapify(max_heap)
        queue = deque()
        time = 0

        # for count in count_map.values():
        #     heapq.heappush(max_heap, -count)

        while max_heap or queue:
            time += 1
            if max_heap:
                t_count = -heapq.heappop(max_heap)
                task_rem = t_count - 1
                if task_rem > 0:
                    queue.append((task_rem, time + n))


            if queue and time == queue[0][1]:
                task_avail = queue.popleft()[0]
                heapq.heappush(max_heap, -task_avail)
        
        return time

