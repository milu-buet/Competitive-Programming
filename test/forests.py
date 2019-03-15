


edges = [(1,2), (1,3), (2,3), (4,5)]
nodes = [1,2,3,4,5]
nbr = { 1:[2,3], 2:[1,3], 3:[1,2,4], 4:[3,5], 5:[4] }

visited = [False]*6
unvisited = {1,2,3,4,5}

#print(visited)

def dfs(start):
	visited[start] = True
	for i in nbr[start]:
		if visited[i] == False:
			unvisited.remove(i)
			dfs(i)


def findUnvisited():
	return unvisited.pop()




def get_forest():
	i=0
	while len(unvisited) > 0:
		i+=1
		dfs(unvisited.pop())
	return i

print(get_forest())