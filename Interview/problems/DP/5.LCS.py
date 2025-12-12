
# f(n,m)  = 1  + f(n-1,n-1) ,if s1[n] == s2[m]:
#		  = max(f(n-1, m), f(n,m-1))
# f(0,m) = 0
# f(n,0) = 0

#   * a b a a c
# * 0 0 0 0 0 0
# b 0
# a 0
# c 0
# a 0 

def LCS(s1, s2):

	n = len(s1)
	m = len(s2)

	dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

	for i in range(1,n+1):
		for j in range(1,m+1):
			if s1[i-1] == s2[j-1]:
				dp[i][j] = 1 + dp[i-1][j-1]
			else:
				dp[i][j] = max(dp[i-1][j], dp[i][j-1])


	return dp[n][m]