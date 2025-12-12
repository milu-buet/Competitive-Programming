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
        
        self.parent = [None]*n
        self.visited = [False]*n
        self.disc = [0]*n
        self.low = [0]*n
        self.order = 0
        self.ans = []
        
        self.dfs(0)
        return self.ans
        
    def dfs(self, u):

        self.visited[u] = True
        self.disc[u] = self.order
        self.low[u] = self.order
        self.order+=1

        for v in self.graph[u]:
            if not self.visited[v]:
                self.parent[v] = u
                self.dfs(v)

                self.low[u] = min(self.low[u], self.low[v])

                if self.low[v] > self.disc[u]:
                    self.ans.append([u,v])

            else:
                if v != self.parent[u]:
                    self.low[u] = min(self.low[u], self.disc[v])