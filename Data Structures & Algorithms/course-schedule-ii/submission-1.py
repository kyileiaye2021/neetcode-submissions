class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        course_map = defaultdict(list)
        course_lst = []
        indegree = [0] * numCourses
        for next_course, prereq in prerequisites:
            course_map[prereq].append(next_course)
            indegree[next_course] += 1

        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
                numCourses -= 1
                course_lst.append(i)

        while queue:
            curr_course = queue.popleft()
            for next_course in course_map[curr_course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)
                    course_lst.append(next_course)
                    numCourses -= 1

        return course_lst if numCourses == 0 else []
        