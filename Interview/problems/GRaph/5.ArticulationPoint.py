class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        
        from collections import defaultdict
        self.graph = defaultdict(list)
        
        for a,b in connections:
            self.graph[a].append(b)
            self.graph[b].append(a)

        self.parents = [None]*n
        self.visited = [False]*n
        self.disc = [0]*n 
        self.low = [0]*n 

        self.time = 0
        self.ans = set()

        for i in range(n):
            self.dfs(i)

        return list(self.ans)


    def dfs(self, u):

        self.visited[u] = True
        children = 0

        self.disc[u] = self.time
        self.low[u] = self.time
        self.time+=1

        for v in self.graph[u]:

            if not visited[v]:
                self.parent[v] = u
                children+=1
                self.dfs(v)

                low[u] = min(low[u], low[v])

                if parent[u] is None and children > 1:
                    self.ans.add(u)

                if parent[u] is not None and low[v] >= disc[u]:
                    self.ans.add(u)
            else:
                if v != parent[u]:
                    low[u] = min(low[u], disc[v])






