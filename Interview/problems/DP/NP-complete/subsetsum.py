
# given a set of numbers A and integer k. Return whether the sum of a subset of A is equal to k.
class Solution(object):
	"""docstring for Solution"""
	def solve(self, nums, k):

		dp = {}
		#return self.dfs(nums, 0, 0, k, dp)

		return self.solveDP2(nums, k)
		


	def dfs(self, nums, i, sm, k):
		if sm == k:
			return True

		elif i == len(nums):
			return False
		return self.dfs(nums, i+1, sm+nums[i], k) or self.dfs(nums, i+1, sm, k)


#    0  1  2  3 ->sum
# 0  t  f  f  f
# 1  t
# 2  t
# 3  t
# 4  t
# 5  t
# 6  t

# i = items taken, j = sum possible?
# F(i,j) = F(i-1, j) or F(i-1, j - A[i-1])

# T(n) = O(n*k)
# S(n) = O(k)

	def solveDP2(self, nums, k):
		n = len(nums)
		mem = [[False for i in range(k+1)] for i in range(2)]

		for i in range(2):
			mem[i][0] = True

		top = 0
		bottom = 1
		for i in range(1,n+1):
			for j in range(1,k+1):
				mem[bottom][j] = mem[top][j]
				if j >= nums[i-1]:
					mem[bottom][j] = mem[bottom][j] or mem[top][j - nums[i-1]]
			top^=1
			bottom^=1

		return mem[top][k]

	def solveDP3(self, nums, k):
		n = len(nums)
		mem = [[False for i in range(k+1)] for i in range(n+1)]

		for i in range(n+1):
			mem[i][0] = True

		for i in range(1,n+1):
			for j in range(1,k+1):
				mem[i][j] = mem[i-1][j]
				if j >= nums[i-1]:
					mem[i][j] = mem[i][j] or mem[i-1][j - nums[i-1]]

		return mem[-1][-1]



# repeated
# f(k) = True
# f(k) = min ( f(k), f(k-nums[j])


	def solveDP_repeated(self, nums, k):

		mem = [ False for i in range(k+1) ]
		mem[0] = True

		for i in range(k+1):
			for j in range(len(nums)):
				if i >= nums[j]:
					mem[i] = mem[i] or mem[i-nums[j]]

		return mem[-1]

	

A = [11,4]
k = 8

print(Solution().dfs(A,0,0,k))
print(Solution().solveDP2(A,k))
print(Solution().solveDP_repeated(A,k))



























###
def sssum(A, k):
	N = len(A)

	Table = [[False for j in range(k+1)] for i in range(2)]
	for i in range(2):
		Table[i][0] = True

	top = 0
	bottom = 1
	for i in range(1,N+1):
		for j in range(1,k+1):
			Table[bottom][j] = Table[top][j]
			if j>=A[i-1]:
				Table[bottom][j] = Table[bottom][j] or Table[top][j-A[i-1]]
		top ^= 1
		bottom ^= 1

	return Table[top][k]


def sssumR(A, k):
	Table = [False for i in range(k+1)]
	Table[0] = True

	for i in range(1,k+1):
		for j in range(len(A)):
			if i>=A[j]:
				Table[i] = Table[i] or Table[i-A[j]]

	return Table[k]


print(sssum([1,5,3,8,6], 300))



		