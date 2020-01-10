class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        def dfs(course):
            if status[course] == 1:
                return False
            if status[course] == 2:
                return True
            status[course] = 1
            for x in graph[course]:
                if not dfs(x):
                    return False
            status[course] = 2
            return True


        graph = [[] for _ in range(numCourses)]
        status = [0 for _ in range(numCourses)]
        for p in prerequisites:
            graph[p[1]].append(p[0])

        for i in range(numCourses):
            if status[i] == 0:
                if not dfs(i):
                    return False
        return True
