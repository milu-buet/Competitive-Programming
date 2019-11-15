

# s1 = 'abcd'
# s2 = 'bcdef'

#   a b c d
# b 0 1 0 0
# c 0 0 2 3
# d 0
# e 0
# f 0

# T(n) = theta(n*m)
# S(n) = theta(n*m)
class Solutions(object):
	"""docstring for Solutions"""
	def solve(self, s1, s2):

		arr = []
		for i in range(len(s2)):
			arr.append([0]*len(s1))

		mx = 0
		for i in range(len(s1)):
			arr[0][i] = int(s1[i]==s2[0])
			mx = max(mx, arr[0][i])

		for i in range(len(s2)):
			arr[i][0] = int(s1[0] == s2[i])
			mx = max(mx, arr[i][0])

		
		for i in range(1,len(s2)):
			for j in range(1, len(s1)):
				if s2[i]==s1[j]:
					arr[i][j] = 1 + arr[i-1][j-1]
					mx = max(mx, arr[i][j])

		return mx


s1 = 'abcd'
s2 = 'bcdef'
X = 'OldSite:GeeksforGeeks.org'
Y = 'NewSite:GeeksQuiz.com'
print( Solutions().solve(X,Y))

# https://www.geeksforgeeks.org/suffix-tree-application-5-longest-common-substring-2/
# with suffix tree it can be done in O(n+m) time and O(n+m) space.
# Ukkonen's Suffix Tree Construction




		