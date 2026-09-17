class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
       # bfs
       # adj list (directed graph)
       # {node: their neighbors with their weights

        # total time len = 0
        # visited = set()

        # push the k node into queue along with time 0 
        # add node k into visited along curr time
        
        # until queue is empty
        #   pop out the node with their time
        #   assign curr time to total time len 
        #   go to the neighbors
        #       check if the neighbor is not already visited
        #       add curr time to the neighbor node time
        #       append to the queue
        #       if the neighbor is already visited
        #           retrieve the already stored neighbor node's time
        #           calculate the neighbor's curr time
        #           get the min of above two and add it to the queue
        # return the total time len if n == len(visited set) else -1


        # we have to create a graph using hashap
        # {curr node: [[nei, time]]}

        # time arr. - inf list with the size of n node
        # add the node k to 0

        # create a min heap to keep track of the min vertex dist
        # add node k with time dist into the min heap

        # until min heap is empty,
        #   pop out the node
        #   go to its nei node 
        #   find the nei time 
        #   if the nei time > curr time + time weight:
        #       update the nei time and add it to the min heap
        #       update the time arr at the vertex position

        # iterate thru the time arr and see if there are nodes we don't cover: return -1
        # else return time

        graph = defaultdict(list)

        for src, des, time in times:
            graph[src].append((des, time))

        # min heap to keep track of the min shortest vertex
        hp = []
        heapq.heappush(hp, (0, k))

        # for storing dist of each vertex
        time_arr = [float('inf')] * (n + 1)
        time_arr[k] = 0

        while hp:
            curr_time_dist, curr_node = heapq.heappop(hp)
            print('curr_node', curr_node)

            # go to the connected node
            for nei, time in graph[curr_node]:
                print('nei:', nei)
                if time_arr[nei] > (curr_time_dist + time):
                    time_arr[nei] = (curr_time_dist + time)
                    heapq.heappush(hp, (time_arr[nei], nei))

        print(time_arr)
        if max(time_arr[1:])!= float('inf'):
            return max(time_arr[1:])

        else:
            return -1








