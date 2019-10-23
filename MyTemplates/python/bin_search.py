
import bisect

def bleft(arr, left, right, val):

	if left > right:
		return left

	mid = (left+right)//2

	if val <= arr[mid]:
		return bleft(arr, left, mid-1, val)
	else:
		return bleft(arr, mid+1, right, val)

def bright(arr, left, right, val):

	if left > right:
		return left

	mid = (left+right)//2

	if val >= arr[mid]:
		return bright(arr, mid+1, right, val)
	else:
		return bright(arr, left, mid-1, val)

data = [11,12,33,33,33,43,54,55,56,87]
#data = [33,33]
print(bleft(data,0,len(data)-1,12))
print(bright(data,0,len(data)-1,12))




# from functools import total_ordering

# @total_ordering
# class cobj(object):
# 	"""docstring for cobj"""
# 	def __init__(self, x1, x2):
# 		self.x1 = x1
# 		self.x2 = x2

# 	def __eq__(self, other):
# 	    return ((self.x1, self.x2) == (other.x1, other.x2))

# 	def __ne__(self, other):
# 	    return not (self == other)

# 	def __lt__(self, other):
# 	    return (self.x2) < (other.x1)

# 	def __gt__(self, other):
# 	    return (self.x1) > (other.x2)

# 	def __repr__(self):
# 	    return "%s %s" % (self.x1, self.x2)



# data = [ cobj(5,6), cobj(7,9) ,cobj(1,4), cobj(11,11)]
# data.sort()

# idx = bisect.bisect(data, cobj(7,9))
# print(idx)

# idx = bisect.bisect_left(data, cobj(7,9))
# print(idx)


# data = [11,12,33,33,33,43,54,55,56,87]
# idx = bisect.bisect(data, 33)  # data[idx-1] <= 33 < data[idx]
# print(idx)
# idx = bisect.bisect_left(data, 33) # data[idx-1] < 33 <= data[idx]
# print(idx)






