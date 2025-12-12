'''
Given a set of cities and distance between every pair of cities, 
the problem is to find the shortest possible route that visits 
every city exactly once and returns to the starting point.
'''

# T(i,j) = T(i,k) + d(k,j), k!=1,j



# ans = min ( T(1,j) + d(1,j) ) 

'''
C(S,i) = 
if S.size==2, 
min: 


T(n) = n*C(n)
C(n) = n*C(n-1)
C(n) = n*2^n

'''

def C(g, S, i, dp):

	if (frozenset(S),i) in dp:
		return dp


	if len(S) == 2:  # S = {0,i}
		return g[0][i] 
	

	mn = float('inf')
	S.remove(i)
	for j in S:
		if j!=0:
			mn = min( mn, C(g, S, j, dp) + g[i][j] )
	S.add(i)

	dp[(frozenset(S),i)] = mn
	return mn


def TSP(g):

	n = len(g)
	S = set(range(n))
	dp = {}

	mn = float('inf')
	for i in range(1,n):
		mn = min(mn, C(g, S, i, dp) + g[0][i]) 

	return mn







g = [ [0, 10, 15, 20],
	  [10, 0, 35, 25],
	  [15, 35, 0, 30],
	  [20, 25, 30, 0]
	]

print(TSP(g))