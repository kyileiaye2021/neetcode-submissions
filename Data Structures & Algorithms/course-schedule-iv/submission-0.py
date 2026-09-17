class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        course_graph = defaultdict(list)
        indeg = [0] * numCourses
        for prereq, course in prerequisites:
            course_graph[prereq].append(course)
            indeg[course] += 1

        queue = deque()
        for i in range(numCourses):
            if indeg[i] == 0:
                queue.append(i)

        prereq_set = {i: set() for i in range(numCourses)}
        while queue:
            curr_course = queue.popleft()

            for neighbor in course_graph[curr_course]:
                prereq_set[neighbor].add(curr_course)
                prereq_set[neighbor].update(prereq_set[curr_course])
                indeg[neighbor] -= 1
                if indeg[neighbor] == 0:
                    queue.append(neighbor)

        res = []
        for (u, v) in queries:
            if u in prereq_set[v]:
                res.append(True)
            else:
                res.append(False)

        return res

        


