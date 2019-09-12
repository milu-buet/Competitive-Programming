
class LStack(object):
	"""docstring for LStack"""
	def __init__(self, limit, alimit):
		self.limit = limit
		self.alimit = alimit
		self.arrs = [[]]

		self.ai = 0
		self.ci = -1


	def push(self,x):

		if self.ai*self.limit + self.ci + 1 < self.alimit:
			if self.ci + 1 < self.limit:
				self.arrs[self.ai].append(x)
				self.ci+=1
			else:
				self.arrs.append(([]))
				self.ai+=1
				self.arrs[self.ai].append(x)
				self.ci = 0


	def pop(self):
		ret = None
		if self.ai*self.limit + self.ci + 1 > 0:
			ret = self.arrs[self.ai].pop(-1)
			if self.ci == 0:
				if self.ai == 0:
					self.ci = -1
				else:
					self.ai-=1
					self.ci = self.limit-1
					self.arrs.pop(-1)
			else:
				self.ci-=1

		return ret
			



st = LStack(2,5)
st.push(3)
st.push(4)
st.push(7)
st.push(5)
st.push(7)
st.push(6)

st.pop()
st.pop()
st.pop()
st.pop()
st.pop()

print(st.arrs)	
