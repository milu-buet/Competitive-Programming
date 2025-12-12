class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        graph = [ [] for _ in range(numCourses) ]
        deg = [ 0 for _ in range(numCourses) ]
        
        
        for a,b in prerequisites:
            graph[a].append(b)
            deg[b]+=1
            
        q = []
        for i in range(numCourses):
            if deg[i]==0:
                q.append(i)
        c  = 0        
        while q:
            i = q.pop(0)
            c+=1
            
            for nb in graph[i]:
                deg[nb]-=1
                if deg[nb]==0:
                    q.append(nb)
                    
        return c==numCourses
            
 
        