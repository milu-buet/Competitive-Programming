
# n choose k
#nCk = n*n-1*...*(n-k+1)/k*k-1*....*1

def calc(n,k):
	if k > n-k:
		k - n-k

	ans = 1

	for i in range(k):
		ans*=(n-i)
		ans/=(i+1)

	return ans