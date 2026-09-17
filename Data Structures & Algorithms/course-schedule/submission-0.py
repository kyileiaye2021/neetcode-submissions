class Solution:
    def createGraph(self, prerequisites):
        graph = collections.defaultdict(list)
        for (course, prereq) in prerequisites:
            graph[prereq].append(course)
        return graph                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # happy cases
        # input: numCourses = 2, prerequisites = [[0,1], [1,0]]
        # output: false

        # input: numCourses = 3, prerequisites = [[1,0], [2,1]]
        # output: true

        # input: numCourses = 3, prerequisites = [[1,0], [2,0]]
        # output: true

        # edge cases
        # input: numCourses = 1, prerequisites = [[0, None]]
        # output: true

        # graph algorithm
        # topological sort
        # direct graph with bfs
        # create graph func {sec: [first]}
        #   iterate thru the prereq pairs
        #      pair the sec ele to the first ele
        #   return the graph

        # create a graph with pairs
        # keep track of the in degree for nodes
        # create a list of size numCourses all initialized to 0
        # iterate thru the graph
        #   for each value in the list
        #       value is index of the list
        #       increment the in deg num in val index position of the list
        # find the nums that have 0 in deg
        # create queue and add those nums to the queue
        # mark those nums as visited
        # iterate until queue is empty
        # pop out the curr node
        #   iterate each neighbor of curr popped out node
        #      if the neighbor is not visited
        #       decrement the in degree
        #       if in deg becomes 0
        #           add the node to the queue
        course_graph = self.createGraph(prerequisites)
        in_deg = [0] * numCourses

        for prereq in course_graph:
            for course in course_graph[prereq]:
                in_deg[course] += 1

        queue = collections.deque()
        for i, val in enumerate(in_deg):
            if val == 0:
                queue.append(i)

        count = 0
        while queue:
            prereq = queue.popleft()
            count += 1

            # go to prereq courses
            for course in course_graph[prereq]:
                in_deg[course] -= 1

                if in_deg[course] == 0:
                    queue.append(course)

        return (count == numCourses)

        


            

