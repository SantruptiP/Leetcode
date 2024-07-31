class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i: [] for i in range(numCourses)}
        
        res = []
        # map each course to : prereq list
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visiting = set()

        def dfs(crs):
            if crs in visiting:
                return False
            if preMap[crs] == []:
                if crs not in res:
                    res.append(crs)
                return True

            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            res.append(crs)
            preMap[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        if res == []:
            for c in range(numCourses):
                res.append(c)
        return res