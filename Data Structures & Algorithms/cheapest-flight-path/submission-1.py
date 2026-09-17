class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        cost = [float('inf')] * n
        cost[src] = 0

        for i in range(k + 1):
            temp_cost = cost.copy()
            for u,v, w in flights:
                if cost[u] != float('inf') and temp_cost[v] > cost[u] + w:
                    temp_cost[v] = cost[u] + w
            cost = temp_cost

        return cost[dst] if cost[dst] != float('inf') else -1
                
        # shortest path from src to des within k stop
        # 
        # BFS (dijstra's algo)
        # min heap
        # cost arr to keep track of the curr cost of airports initialized to inf
        # add the src to min heap with cost of 0
        # 
        # while min heap
        #   pop out the curr airport with the curr cost
        #   for i in range(len(min_hea)):
            #   for each nei airport
            #       check if the cost of nei airport is > the cost of cur airport + cost to nei airport
            #           update the cost of nei airport
        #   decrement k
        #   if k == -1:
        #   break

        # return the cost at the des airport if it is not inf else -1
        # adj_lst = {i:[] for i in range(n)}
        # for u,w,c in flights:
        #     adj_lst[u].append((w, c))
        # print(adj_lst)
        # pq = []

        # cost = [float('inf')] * n
        # heapq.heappush(pq, (0, src, 0)) # (dist, src, stop_used)
        # cost[src] = 0

        # while pq:         

        #     curr_cost, curr_airport, curr_stop = heapq.heappop(pq)
        #     print('Curr cost', curr_cost)

        #     for nei_airport, nei_cost in adj_lst[curr_airport]: 
                
        #         if  cost[nei_airport] > curr_cost + nei_cost:
        #             cost[nei_airport] = curr_cost + nei_cost
        #             print(cost[nei_airport])
        #             if curr_stop < k:
        #                 heapq.heappush(pq, (cost[nei_airport], nei_airport, curr_stop + 1))
                
        
        # return cost[dst] if cost[dst] != float('inf') else -1





    