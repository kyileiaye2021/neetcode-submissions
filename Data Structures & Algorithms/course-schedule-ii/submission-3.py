class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        graph_map = {i: [] for i in range(numCourses)}

        for next_c, prereq_c in prerequisites:
            graph_map[prereq_c].append(next_c)
            indegree[next_c] += 1

        queue = deque()
        res_list = []

        for i, pre in enumerate(indegree):
            if pre == 0:
                queue.append(i)

        while queue:
            cur_course = queue.popleft()
            numCourses -= 1
            res_list.append(cur_course)

            for next_c in graph_map[cur_course]:
                indegree[next_c] -= 1
                if indegree[next_c] == 0:
                    queue.append(next_c)
        
        return res_list if numCourses == 0 else []

        # course_map = defaultdict(list)
        # course_lst = []
        # indegree = [0] * numCourses
        # for next_course, prereq in prerequisites:
        #     course_map[prereq].append(next_course)
        #     indegree[next_course] += 1

        # queue = deque()
        # for i in range(numCourses):
        #     if indegree[i] == 0:
        #         queue.append(i)
        #         numCourses -= 1
        #         course_lst.append(i)

        # while queue:
        #     curr_course = queue.popleft()
        #     for next_course in course_map[curr_course]:
        #         indegree[next_course] -= 1
        #         if indegree[next_course] == 0:
        #             queue.append(next_course)
        #             course_lst.append(next_course)
        #             numCourses -= 1

        # return course_lst if numCourses == 0 else []
        