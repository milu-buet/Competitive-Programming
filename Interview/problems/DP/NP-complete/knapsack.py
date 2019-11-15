# Given a set of items, each with a weight and a value, 
# determine the number of each item to include in a collection so that the 
# total weight is less than or equal to a given limit and the total value is as large as possible

# Weights = [3,2,1,5,6,8]
# Values =  [3,1,6,2,3,9]
# WeightLimit = 20



class Solutions(object):
	"""docstring for Solutions"""

	def solve(self, w, v, k):

		self.mx = float('-inf')
		self.dfs(w, v, 0, 0, 0, k)
		return self.mx


	def dfs(self, w, v, i, ws, vs, k):

		if ws > k:
			return

		self.mx = max(self.mx, vs)

		if i == len(w):
			return

		self.dfs(w, v, i+1, ws+w[i], vs+v[i] ,k)
		self.dfs(w, v, i+1, ws, vs ,k)


# f(i,k) = max ( f(i-1,k), v[i-1]+f(i-1,k-w[i-1]) )
# f(i,0) = 0
# f(0,k) = 0
# No repeatation
# T(n) = O(n*k)
# s(n) = O(k)

	def dp(self, w, v, k):

		n = len(w)
		mem = [ [0 for i in range(k+1)] for i in range(2)]

		top = 0
		bottom = 1
		for i in range(1,n+1):
			for j in range(1,k+1):
				mem[bottom][j] = mem[top][j]
				if j >= w[i-1]:
					mem[bottom][j] = max(mem[bottom][j], v[i-1] + mem[top][j-w[i-1]])
			top^=1
			bottom^=1

		return mem[top][-1]


# repeated allowed
# f(k) = max( f(k), v[0]+f(k-w[0]), v[1]+f(k-w[1]), .... )

	def dp_repeated(self, w, v, k):
		mem = [0 for i in range(k+1)]
		for i in range(k+1):
			for j in range(len(w)):
				if i >= w[j]:
					mem[i] = max( mem[i], v[j] + mem[i - w[j]])

		return mem[-1]






def kp(w, v, k):

	n = len(w)
	dp = [ [0 for i in range(k+1)] for j in range(n+1) ]

	for i in range(1,n+1):
		for j in range(1,k+1):
			dp[i][j] = dp[i-1][j]
			if j >= w[i-1]:
				dp[i][j] = max( dp[i][j], v[i-1] + dp[i-1][j-w[i-1]] )
	return dp[-1][-1]




def kpr(w,v,k):
	n = len(w)

	dp = [ 0 for i in range(k+1) ]

	for i in range(k+1):
		for j in range(n):
			if i>= j:
				dp[i] = max( dp[i], v[j] + dp[i-w[j]] )










v = [60, 100, 120] 
w = [10, 20, 30] 
k = 50
print(Solutions().solve(w,v,k))
print(Solutions().dp(w,v,k))
print(Solutions().dp_repeated(w,v,k))
print(kp(w,v,k))



