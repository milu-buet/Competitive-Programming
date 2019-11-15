'''

ABCDE
(A)(BCDE)
(AB)(CDE)
(ABC)(DE)
(ABCD)(E)

ith mat,
jth mat,
f(i,j) =  min => k=i...j-1, f(i,k) + f(k+1,j) + A[i-1]*A[k]*A[j] 
f(i,i) = 0


f(1,n)
f(1,1), f(2,n), f(1,2), f(3,n) 

'''



def solve(A):

	dp = {}
	n = len(A)-1

	for i in range(1,n+1):
		dp[(i,i)] = 0

	for size in range(2,n+1):
		for i in range(1,n+2-size):
			j = i+size-1
			if i==j:
				dp[(i,j)] = 0
			else:
				dp[(i,j)]= float('inf')
				for k in range(i,j):
					dp[(i,j)] = min( dp[(i,j)], dp[(i,k)] + dp[(k+1,j)] + A[i-1]*A[k]*A[j] )

	return dp[(1,n)]



A = [40, 20, 30, 10, 30]
A = [1, 2, 3, 4]
print(solve(A))



'''
ABCDE
(A)(BCDE)
(AB)(CDE)
(ABC)(DE)
(ABCD)(E)

f(i,j) = k:i...j-1,  f(i,k) + f(k+1,j) + A[i-1]*A[k]*A[j]
f(i,i) = 0

f(1,n) = ?


'''

def solve(A):

