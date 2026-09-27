class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # topological sort

        dq = collections.deque()

        # hashmap {course: prereq}
        next_courses = defaultdict(list)
        prereq_num = [0] * numCourses
        for c, p in prerequisites:
            next_courses[p].append(c)

            prereq_num[c] += 1
    
        for c, count in enumerate(prereq_num):
            if count == 0:
                dq.append(c)

        course_count = 0
        while dq:
            curr_course = dq.popleft()
            course_count += 1

            print(curr_course)
            for next_course in next_courses[curr_course]:
                prereq_num[next_course] -= 1
                if prereq_num[next_course] == 0:
                    dq.append(next_course)

        return course_count == numCourses

        
