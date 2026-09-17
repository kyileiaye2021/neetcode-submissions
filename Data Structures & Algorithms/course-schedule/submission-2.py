class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        indegree = [0] * numCourses
        graph_map = {i: [] for i in range(numCourses)}

        for next_c, prereq_c in prerequisites:
            graph_map[prereq_c].append(next_c)
            indegree[next_c] += 1

        queue = deque()

        for i, pre in enumerate(indegree):
            if pre == 0:
                queue.append(i)

        while queue:
            cur_course = queue.popleft()
            numCourses -= 1

            for next_c in graph_map[cur_course]:
                indegree[next_c] -= 1
                if indegree[next_c] == 0:
                    queue.append(next_c)
        
        return True if numCourses == 0 else False






        # # topological sorting using kahn's algorithm
        # # bfs
        # # create a queue
        # # create a hashmap {prereq: courses}
        # # keep track of the indeg values of courses
        # # store the courses with no prereq into the queue
        # #   pop out the course
        # #   for each next course of the cur course
        # #       check if the indeg of next course becomes 0, add them to the queu
        
        # # time complexity - O(V + E)
        # # space complexity - O(V + E)
        # course_graph = defaultdict(list)
        # indeg = [0] * numCourses

        # for (course, prereq) in prerequisites:
        #     course_graph[prereq].append(course)
        #     indeg[course] += 1

        # queue = collections.deque()
        # course_count = 0
        # for i in range(numCourses):
        #     if indeg[i] == 0:
        #         queue.append(i)

        # while queue:
        #     curr_course = queue.popleft()
        #     course_count += 1
        #     for next_course in course_graph[curr_course]:
        #         indeg[next_course] -= 1
        #         if indeg[next_course] == 0:
        #             queue.append(next_course)

        # return numCourses == course_count

            



        
