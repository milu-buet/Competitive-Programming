


# (1,2), (2,4), (2,1)
# 1


class Solution(object):
	"""docstring for Solution"""

	def solve(self, edges):

		mem = set()
		ans = 0
		for a,b in edges:
			if (b,a) in mem:
				ans+=1

			mem.add((a,b))

		return ans

		