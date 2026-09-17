class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # happy cases
        # tasks = ["X", "X", "Y", "Y"]
        # n = 2
        # X-> Y -> idle -> X -> Y

        # tasks = ["A", "A", "A", "B", "C"]
        # n = 3
        # A -> B -> C -> idle -> A -> idle -> idle -> idle -> A

        # edge cases
        # tasks = ["A", "A", "B"]
        # n = 0
        # A -> A -> B
        # 3

        # tasks = ["A", "A", "B"]
        # n = 1
        # A -> B -> A
        # 3

        # tasks = ["A"]
        # n = 0
        # A
        # 1

        # need to do most freq job first so that we don't have a lot of idle
        # need to know the freq of the task
        # max heap to do the most freq task first
        # need to track of the time for each task to put the same task back in line 
        # task freq will be decremented at a time and time will be incremented
        # return the time

        task_freq = Counter(tasks)

        freq = [-f for f in task_freq.values()]
        heapq.heapify(freq)

        time = 0
        queue = deque()
        while freq or queue:
            time += 1
            # pop out the most freq task
            if freq:
                temp = -heapq.heappop(freq)

                # decrement the task
                remaining = temp - 1

                if remaining > 0: # there are still same tasks to do
                    # store the same task with the time when it will be put back in line
                    queue.append([remaining, (time + n)])

            if queue:
                if queue[0][1] == time:
                    remaining = -queue.popleft()[0]
                    heapq.heappush(freq, remaining)

        return time

            


        