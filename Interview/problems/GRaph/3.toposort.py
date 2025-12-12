class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        from collections import defaultdict
        
        graph = defaultdict(list)
        deg = defaultdict(int)
        
        
        for a,b in prerequisites:
            graph[a].append(b)
            deg[b]+=1
            
        q = []
        for i in range(numCourses):
            if deg[i]==0:
                q.append(i) 
        ans = []
        while q:
            i = q.pop(0)
            ans.append(i)
            
            for nb in graph[i]:
                deg[nb]-=1
                if deg[nb]==0:
                    q.append(nb)
        
        if len(ans) == numCourses:
            return ans[::-1]
        
        return []
            
        