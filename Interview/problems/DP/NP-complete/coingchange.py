# Given coins[] and amount, return minimum number of coins to make the amount.
# coins = [1, 2, 5], amount = 11
# ans = 5 + 5 + 1 => 3

# k=amount
# C=coins
# f(k) = 1 + min(f(k-C[j]) )
# f(0) = 0

class Solution(object):

	def dp(self, coins, amount):
		
		mem = [ float('inf') for i in range(amount+1) ]
		mem[0] = 0

		for i in range(1,amount+1):
		    for j in range(len(coins)):
		        if i >= coins[j]:
		            mem[i] = min( mem[i], 1 + mem[i-coins[j]])

		if mem[amount] != float('inf'):
		    return mem[amount]
		return -1

coins = [1,5]
amount = 11
print(Solution().dp(coins, amount))

############################################################################
# Given coins[] and amount, return a list (minimum) of coins which to make the amount.
# coins = [1, 2, 5], amount = 11
# ans = 5 + 5 + 1 => 3

# k=amount
# C=coins
# f(k) = [C[j]] + min_size(f(k-C[j]))
# f(0) = []

class Solution(object):

	def dp(self, coins, amount):
		
		mem = [ [None]*(amount+1) for i in range(amount+1) ]
		mem[0] = []

		for i in range(1,amount+1):
		    for j in range(len(coins)):
		        if i >= coins[j] and len(mem[i]) > len(mem[i-coins[j]]):
		            mem[i] = [coins[j]] + mem[i-coins[j]]

		if len(mem[amount]) < amount+1:
		    return mem[amount]
		
		return -1

coins = [1,5]
amount = 11
print(Solution().dp(coins, amount))


#############################################################################
# Given coins[] and amount, return number of all possible ways of changes to make the amount.
# coins = [1, 5], amount = 6
# ans = 2 # (111111),(1 5)

# k = amount
# C = coins
# n = # of coins
# i = coin id 
# f(i, k) = f(i-1, k) + f(i, k-C[i-1])
# f(0, k) = 0
# f(i, 0) = 1

class Solution(object):
	def dp(self, coins, amount):

		n = len(coins)
		dp = [[0 for k in range(amount+1)] for i in range(n+1)]
		
		for k in range(amount+1):
			dp[0][k] = 0

		for i in range(n+1):
			dp[i][0] = 1

		for i in range(1,n+1):
			for k in range(1,amount+1):
				dp[i][k] = dp[i-1][k]
				if coins[i-1] <= k:
					dp[i][k] += dp[i][k-coins[i-1]]

		return dp[n][amount]


coins = [1,5]
amount = 6
# 111111, 15
print(Solution().dp(coins, amount))
#######################################################################################

def coinChange(coins, i, M, current, ans):

	if M==0:
		ans.append(list(current))
	elif i==len(coins):
		return

	for k in range(1,M+1):
		if coins[i]*k > M:
			break

		current += [coins[i]]*k
		coinChange(coins, i+1, M-coins[i]*k, current, ans)
		
		for p in range(k):
			current.pop()



coins = [1,2,5,10]
M = 3
ans = []
current = []

coinChange(coins, 0, M, current, ans)
print(ans)













