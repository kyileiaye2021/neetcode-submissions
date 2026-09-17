class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        maxHeap = []

        freq_count = Counter(tasks)

        for count in freq_count.values():
            maxHeap.append(-count)

        heapq.heapify(maxHeap)

        queue = deque()
        time = 0

        while maxHeap or queue:
            time += 1

            if maxHeap:
                task = -heapq.heappop(maxHeap)
                rem_task = task - 1

                if rem_task > 0:
                    queue.append((rem_task, time + n))


            if queue and time == queue[0][1]:
                rem_task, time = queue.popleft()
                heapq.heappush(maxHeap, -rem_task)

        return time

            