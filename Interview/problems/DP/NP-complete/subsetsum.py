
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


#    0  1  2  3
# 0  t  f  f  f
# 1  t
# 2  t
# 3  t
# 4  t
# 5  t
# 6  t

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


		