
import bisect

data = [11,12,33,33,33,43,54,55,56,87]
idx = bisect.bisect(data, 33)  # data[idx-1] <= 33 < data[idx]
print(idx)
idx = bisect.bisect_left(data, 33) # data[idx-1] < 33 <= data[idx]
print(idx)




from functools import total_ordering

@total_ordering
class cobj(object):
	"""docstring for cobj"""
	def __init__(self, x1, x2):
		self.x1 = x1
		self.x2 = x2

	def __eq__(self, other):
	    return ((self.x1, self.x2) == (other.x1, other.x2))

	def __ne__(self, other):
	    return not (self == other)

	def __lt__(self, other):
	    return (self.x2) < (other.x1)

	def __gt__(self, other):
	    return (self.x1) > (other.x2)

	def __repr__(self):
	    return "%s %s" % (self.x1, self.x2)



data = [ cobj(5,6), cobj(7,9) ,cobj(1,4), cobj(11,11)]
data.sort()

idx = bisect.bisect(data, cobj(7,9))
print(idx)

idx = bisect.bisect_left(data, cobj(7,9))
print(idx)
