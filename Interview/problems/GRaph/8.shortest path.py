

import heapq
from collections import defaultdict
class Solutions(object):
	"""docstring for Solutions"""
	def shortestpath(self, s, edges):

		graph = defaultdict(list)
		wt = {}

		for a,b,w in edges:
			graph[a].append(b)
			graph[b].append(a)
			wt[(a,b)] = w
			wt[(b,a)] = w


		d = {}
		q = [(0,s)]
		visited = set()


		while q:
			dist, u = heapq.heappop(q)
			if u in visited:
				continue

			d[u] = dist
			visited.add(u)
			for v in graph[u]:
				if v not in visited:
					heapq.heappush(q, (dist+wt[(u,v)], v) )


		print(d)



edges = [['A', 'B', 6], ['A','D', 1], ['B', 'D', 2], ['D', 'E', 1], ['B', 'E', 2], ['E', 'C', 5], ['B', 'C', 5]]
Solutions().shortestpath('A', edges)




		