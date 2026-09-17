class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        # heapify the items
        
        # id = 0
        # res
        # total = 0
        
        # while items are not empty
        # check if the id not already visited
            # for _ in 5 times
            #   pop out the items
            # calculate the total avg
            # add the [id, total avg] to res
            # mark id as visited
        # else
        #   pop out

        # return res

        # id = 0
        # res = []

        # heapq.heapify(items)

        # print(items)

        # while len(items) > 0:
        #     cur_id = items[0][0]
        #     if cur_id != id:

        #         total = 0

        #         for i in range(5):
        #             cur_id, score = heapq.heappop(items)
        #             total += score

        #         id = cur_id
        #         res.append([cur_id, total // 5])

        #     else:
        #         heapq.heappop(items)
        
        # return res

        # map: {id: max heap(scores)}
        res = []
        score_map = {}
        for id, score in items:
            if id in score_map:
                heapq.heappush(score_map[id], -score)
            
            else:
                score_map[id] = [-score]

        print(score_map)

        for id, score in score_map.items():
            total = 0

            for _ in range(5):
                total += -heapq.heappop(score)

            heapq.heappush(res, [id, total // 5])
        
        return res

            


            
