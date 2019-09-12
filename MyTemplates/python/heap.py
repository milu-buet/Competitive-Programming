
import heapq


# min heap numbers or obj
# priority queue
class MinHeap(object):
  def __init__(self): self.h = []
  def push(self,x): heapq.heappush(self.h,x)
  def pop(self): return heapq.heappop(self.h)
  def __getitem__(self,i): return self.h[i]
  def __len__(self): return len(self.h)

#------------------------------------------------------------
minh = MinHeap()
minh.push(5)
minh.push(2)
minh.push(8)
print(minh.pop())


#--------------------------------------------------------------
# max heap for numbers
class MaxHeap(object):
  def __init__(self): self.h = []
  def push(self,x): heapq.heappush(self.h, x*-1)
  def pop(self): return heapq.heappop(self.h)*-1
  def __getitem__(self,i): return self.h[i]
  def __len__(self): return len(self.h)

maxh = MaxHeap()
maxh.push(5)
maxh.push(2)
maxh.push(8)
print(maxh.pop())

#----------------------------------------------------------------
# max heap obj

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

	def __mul__(self, other):
		return cobj(-1*self.x1, -1*self.x2)


maxh = MaxHeap()
maxh.push(cobj(7,8))
maxh.push(cobj(1,5))
maxh.push(cobj(6,6))
print(maxh.pop())