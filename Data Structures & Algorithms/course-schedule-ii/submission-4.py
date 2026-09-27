class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # topological sort 
        # bfs
        can_take = collections.deque()
        # prereq: next courses
        next_courses = defaultdict(list)
        prereq_num = [0] * numCourses

        for course, prereq in prerequisites:

            next_courses[prereq].append(course)
            prereq_num[course] += 1

        for course, count in enumerate(prereq_num):
            if count == 0:
                can_take.append(course)

        course_count = 0
        res = []
        while can_take:
            curr_course = can_take.pop()
            res.append(curr_course)
            course_count += 1

            for next_course in next_courses[curr_course]:
                prereq_num[next_course] -= 1
                if prereq_num[next_course] == 0:
                    can_take.append(next_course)

        return res if course_count == numCourses else []

    