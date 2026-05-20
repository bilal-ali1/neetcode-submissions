class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        coursesToPre = {}
        for i in range(numCourses):
            coursesToPre[i] = []

        for course in prerequisites:
            coursesToPre[course[0]].append(course[1])
        
        res = []
        visitingSet = set()
        visitedSet = set()

        def dfs(course):
            if course in visitingSet:
                return False
            
            if course in visitedSet:
                return True
        
            visitingSet.add(course)
            visitedSet.add(course)
            if coursesToPre[course] == []:
                visitingSet.remove(course)
                res.append(course)
                return True
            
            for pre in coursesToPre[course]:
                if not dfs(pre):
                    return False

            visitingSet.remove(course)
            coursesToPre[course] = []
            res.append(course)
            return True
        
        for course in coursesToPre:
            if not dfs(course):
                return []
        
        return res
