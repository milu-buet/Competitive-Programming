'''
You are given a set of n types of rectangular 3-D boxes, 
where the i^th box has height h(i), width w(i) and depth d(i) (all real numbers). 
You want to create a stack of boxes which is as tall as possible, 
but you can only stack a box on top of another box if the dimensions of 
the 2-D base of the lower box are each strictly larger than those of the 2-D base of the higher box. 
Of course, you can rotate a box so that any side functions as its base.
 It is also allowable to use multiple instances of the same type of box.


box(i) = base(i),h(i)
base(i) = min(w(i), d(i)), max(w(i), d(i))

O(nlogn)
sort boxes by their bases

n boxes: 0, 1, ..... , n-1

begining at box i
f(i) = h(i) + max( f(j), j=i+1...n-1, base(i)<base(j) )
'''

# T(n) = O(n^2)

def solve(A):

	B = []
	n = len(A)
	for i in range(n):
		h,w,d = A[i]

		x = min(w,d), max(w,d), h
		B.append(x)

		x = min(h, d), max(h, d), w
		B.append(x)

		x = min(w ,h), max(w, h), d
		B.append(x) 


	A = B
	n = len(A)
	A.sort()
	dp = [0]*len(A)

	for i in range(n-1, -1, -1):
		mx = 0
		for j in range(i+1, n):
			if A[i][0] < A[j][0] and A[i][1]<A[j][1]:
				mx = max(mx, dp[j])
		dp[i] = A[i][2] + mx

	return max(dp)

A = [ [4, 6, 7], [1, 2, 3], [4, 5, 6], [10, 12, 32] ]
print(solve(A))