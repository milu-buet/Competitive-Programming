
'''
Partition a set into two subsets such that the difference of subset sums is minimum
output = minumum difference
A = [1,5,2,4,2,-2,10]


tot = sum(A)

f(n, tot) = ?
f(n, sm) = min ( f(n-1, sm),  f(n-1, sm-A[n]) )
f(0, sm) =  abs(tot - 2*sm) 


'''

def solve(A):

	n = len(A)
	tot = sum(A)

	dp = {}

	for i in range(n+1):
		for j in range(tot+1):
			if i == 0:
				dp[(i,j)] = abs(tot - 2*j)
			else:
				dp[(i,j)] = dp[(i-1,j)]
				if j >= A[i-1]:
				 	dp[(i,j)]	= min(dp[(i,j)], dp[(i-1,j-A[i-1])] )


	return dp[(n,tot)]


A = [1,5,2,4,2,-2,10]
print(solve(A))