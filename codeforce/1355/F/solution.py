import sys
from collections import defaultdict
import math
import random
M = 1000000000
MM = 1000000000000000000
class Solution(object):

	def __init__(self, X=None):
		if X is None:
			sys.stdout.flush()
		self.X = X

	def solve(self):  # 80% accuracy

		cur = 1 
		for i in range(22):
			Q1 = random.randint(1, M)
			Q2 = random.randint(1, M)
			Q = Q1*Q2
			n = Q
			while n<=MM:
				n *= Q
			n /= Q

			cur = self.LCD(cur, self.guessGCD2(n))

		self.cur = cur
		ans = self.getDivisorCount(cur)
		return max(2*ans, ans+7)
	

	def guessGCD(self, Q):
		print("? "+str(Q))
		return int(input())

	def guessGCD2(self, Q):
		return self.GCD(Q,X)


	def LCD(self, x, y):
		return (x*y)/self.GCD(x, y)

	def GCD(self, x, y): # x>=y
		if x<y:
			x,y = y,x
		if x%y==0: return y
		return self.GCD(y, x%y)

	def getDivisorCount(self, n):
		
		ans = 1
		if 0<=n<=1:
			return ans

		c = 0
		while n%2 == 0:
			n /= 2
			c += 1
		ans *= (c+1)

		n_sqr = int(math.sqrt(n)) + 1
		for i in range(3,  n_sqr, 2):
			c = 0
			while n%i ==0:
				n /= i
				c += 1
			ans *= (c+1)

		return ans

	def verify(self):
		ans = self.solve()
		d = self.getDivisorCount(self.X)

		f = .5 <= float(ans)/d <= 2.0 or abs(ans-d) <= 7

		if not f:
			pass
			print((self.cur,ans), (self.X,d))

		return f



#print(Solution().getDivisorCount(1000000000))

c = 1.0
t=100
for i in range(t):
	X = random.randint(1, 1000000000)
	res = Solution(X).verify()
	#print(X, res)
	c += int(res)


print(c/t)

# t=1000
# obj = Solution()
# for i in range(2,t):
# 	print(i, obj.getDivisorCount(i))


# def getFact(n):
	
# 	ans = []
# 	if 0<=n<=1:
# 		return ans

# 	while n%2 == 0:
# 		n /= 2
# 		ans.append(2)
		

# 	n_sqr = int(math.sqrt(n)) + 1
# 	for i in range(3,  n_sqr, 2):
# 		while n%i ==0:
# 			n /= i
# 			ans.append(i)

# 	return ans

# nums = [19634730635520000, 67665248476907597, 877779077635511999, 15031861979012587, 239868713978954299, 8100049778130103, 32826117705688133, 96265407405451883, 260006624961107813, 707992818804600227, 3676594834162829, 6402204344683229, 9797084445859807, 15916020492768661, 27616086651273059, 41286304414422503, 229580147]
# for n in nums:
# 	print(getFact(n))