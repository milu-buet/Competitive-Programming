'''
Count the number of ways we can parenthesize the expression so that the value of expression evaluates to true.

A = "TFT"
B = "^&"

f(i,j) = sum => k:i..j-1  : f(i,k)=f1,t1   f(k+1,j)=f2,t2
if B[k] == '^':
	T = f1*t2 + f2*t2
	F = f1*f1 + t2*t2
elif B[k] == '&':


f(i,i) = if A[i]=='T' ret: 1,0 else 0,1


'''

def solve(A,B):

	n = len(A)

	dp = {}
	for i in range(n):
		if A[i] == 'T':
			dp[(i,i)] = 1,0
		else:
			dp[(i,i)] = 0,1


	for size in range(2,n+1):
		for i in range(0,n+1-size):
			j = i+size-1
			t,f = 0,0
			for k in range(i,j):
				t1,f1 = dp[(i,k)]
				t2,f2 = dp[(k+1,j)]
				if B[k] == '^':
					t += f1*t2 + t1*f2
					f += f1*f2 + t1*t2
				elif B[k] == '&':
					t += t1*t2
					f += t1*f2 + f1*t2 + f1*f2
				elif B[k] == '|':
					t += t1*t2 + t1*f2 + f1*t2
					f += f1*f2

			dp[(i,j)] = t,f

	print(dp)
	T,F = dp[(0,n-1)]

	return T


A = "TTFT"
B = "|&^"
print(solve(A,B))