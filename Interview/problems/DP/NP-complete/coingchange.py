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


# C = coins
# n = # of coins

# i = coin id 
# k = amount
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


coins = [1,2,5,10]
amount = 11 #amount to make
# 111111, 15
print(Solution().dp(coins, amount))









#######################################################################################
# Given coins[] and amount, return all possible ways of changes to make the amount.
# coins = [1, 2, 5, 10], amount = 3
# ans = [[1, 2], [1, 1, 1]]

def coinChange(coins, i, amount, current, ans):

	if amount < 0:
		return
	elif amount == 0:
		ans.append(list(current))
		return
	elif i==len(coins):
		return

	k = 0
	while amount >= k*coins[i]:
		current += [coins[i]]*k
		coinChange(coins, i+1, amount-k*coins[i], current, ans)
		
		for p in range(k):
			current.pop()
		k+=1



coins = [1,2,5,10]
amount = 11 #amount to make
ans = []
current = []

coinChange(coins, 0, amount, current, ans)
print(ans)



'''
f(i, m) = f(i-1,m- 0*coins[i]) + f(i-1, m-1*coins[i]) + f(i-1, m-2*coins[i])
'''
def cn(coins, amount):
	dp = [[0 for j in range(amount+1)] for i in range(len(coins)+1)]

	for i in range(len(coins)+1):
		dp[i][0] = 1

	for j in range(1,amount+1):
		for i in range(1, len(coins)+1):
			k=0
			while j >= k*coins[i-1]:
				dp[i][j] += dp[i-1][j-k*coins[i-1]]
				k+=1
	return dp[-1][-1]

print(cn([1,2,5,10], 11))












