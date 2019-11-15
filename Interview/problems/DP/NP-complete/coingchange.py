
# Given coins[] and amount, return minimum number of coins to make the amount.
# coins = [1, 2, 5], amount = 11
# ans = 5 + 5 + 1 => 3


# f(k) = min( 1 + f(k-C[j]) )
# f(0) = 0
# T(n) = 

class Solution(object):

	def dp(self, coins, amount):
		
		mem = [ float('inf') for i in range(amount+1) ]
		mem[0] = 0

		for i in range(amount+1):
		    for j in range(len(coins)):
		        if i >= coins[j]:
		            mem[i] = min( mem[i], 1 + mem[i-coins[j]])

		if mem[-1] != float('inf'):
		    return mem[-1]

		return -1

	def __init__(self):
	    self.ret = float('inf')
	    
	def coinChange(self, coins, amount):
	    
	    def helper(num_coins, need, start):
	        
	        need_largest_coin = need // coins[start]
	        if num_coins + need_largest_coin >= self.ret:
	            return
	        if need % coins[start] == 0:
	            self.ret = min(self.ret, need // coins[start] + num_coins)
	            return
	        if start == len(coins) - 1:
	            return
	        for num_used in range(need_largest_coin, -1, -1):
	            helper(num_coins + num_used, need - coins[start] * num_used, start + 1)

	    coins = sorted(coins, reverse=True)
	    helper(0, amount, 0)
	    
	    return self.ret if self.ret < float('inf') else -1


coins = [5]
amount = 11
print(Solution().dp(coins, amount))






