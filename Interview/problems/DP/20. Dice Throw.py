'''
Given n dices each with m faces, numbered from 1 to m, 
find the number of ways to get sum X. X is the summation of values on each face when all the dice are thrown.


f(i, X) = j=1...m, sum(f(i-1,X-j))

f(i, i) = 1
f(i, X) = 0 if X<i
f(0, X) = 0
'''


def solve(m, n, X):

	dp = {}

	for i in range(n+1):
		for x in range(X+1):
			if i==x:
				dp[(i,x)] = 1
			elif x < i:
				dp[(i,x)] = 0
			elif i==0:
				dp[(i,x)] = 0
			else:
				dp[(i,x)] = 0
				for j in range(1,m+1):
					if x>=j:
						dp[(i,x)] += dp[(i-1,x-j)]

	return dp[(n,X)]




print(solve(4, 3, 5))