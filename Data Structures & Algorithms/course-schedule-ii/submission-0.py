class Solution:
    def createGraph(self, prerequisites):
        graph = collections.defaultdict(list)
        for (course, prereq) in prerequisites:
            graph[prereq].append(course)
        return graph    

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course_graph = self.createGraph(prerequisites)

        # num of in-deg prereqs for each courses
        in_deg = [0] * numCourses
        for prereq in course_graph:
            for course in course_graph[prereq]:
                in_deg[course] += 1

        res = []
        queue = collections.deque()
        for i, val in enumerate(in_deg):
            if val == 0:
                queue.append(i)
                res.append(i)

        count = 0
        while queue:
            prereq = queue.popleft()
            count += 1

            # go to prereq courses
            for course in course_graph[prereq]:
                in_deg[course] -= 1

                if in_deg[course] == 0:
                    queue.append(course)
                    res.append(course)

        if (count == numCourses):
            return res
        else:
            return []

        


            

