class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        coursesToPre = {}
        for i in range(numCourses):
            coursesToPre[i] = []
        
        for course in prerequisites:
            coursesToPre[course[0]].append(course[1])
        
        print(coursesToPre)
        visitingSet = set()

        def dfs(course):
            if course in visitingSet:
                return False
            visitingSet.add(course)
            if coursesToPre[course] == []:
                visitingSet.remove(course)
                return True
            for prereq in coursesToPre[course]:
                if not dfs(prereq):
                    return False
            coursesToPre[course] = []
            visitingSet.remove(course)
            return True

        for course in prerequisites:
            if not dfs(course[0]):
                return False
        return True
