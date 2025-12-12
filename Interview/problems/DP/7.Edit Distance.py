
# f(n,m) = f(n-1,m-1) if s1[n-1]==s2[m-1]
# 		 =  1 + min {f(n-1,m), f(n,m-1), f(n-1,m-1)}
# f(n,0) = n
# f(0,m) = m

# T(n,m) = O(n*m)
# S(n,m) = O(n*m)

def editDistance(s1, s2):
	n = len(s1)
	m = len(s2)
	dp = [[ float('inf') for j in range(m+1)] for i in range(n+1)]

	for i in range(n+1):
		dp[i][0] = i
	for j in range(m+1):
		dp[0][j] = j

	for i in range(1,n+1):
		for j in range(1,m+1):
			if s1[i-1] == s2[j-1]:
				dp[i][j] = dp[i-1][j-1]
			else:
				dp[i][j] = 1 + min( dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
	return dp[n][m]



print(editDistance("abcd","adc"))

