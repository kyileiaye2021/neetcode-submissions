class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # topological sorting using kahn's algorithm
        # bfs
        # create a queue
        # create a hashmap {prereq: courses}
        # keep track of the indeg values of courses
        # store the courses with no prereq into the queue
        #   pop out the course
        #   for each next course of the cur course
        #       check if the indeg of next course becomes 0, add them to the queu
        
        course_graph = defaultdict(list)
        indeg = [0] * numCourses

        for (course, prereq) in prerequisites:
            course_graph[prereq].append(course)
            indeg[course] += 1

        queue = collections.deque()
        course_count = 0
        for i in range(numCourses):
            if indeg[i] == 0:
                queue.append(i)

        while queue:
            curr_course = queue.popleft()
            course_count += 1
            for next_course in course_graph[curr_course]:
                indeg[next_course] -= 1
                if indeg[next_course] == 0:
                    queue.append(next_course)

        return numCourses == course_count

            



        
