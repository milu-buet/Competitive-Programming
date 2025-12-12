

def succ(root, target):

	if root is None:
		return None

	if target == root.val:
		if root.right is not None:
			return root.right
		return None

	elif target < root.val:
		if succ(root.left, target) is None:
			return root
	else:
		return succ(root.right, target)



class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None



n1 = Node(5)
n2 = Node(2)
n3 = Node(6)

n1.left = n2
n1.right = n3


print(succ(n1, 2).val)



def t2array(ar1, ar2, n):

	if n > len(ar1) + len(ar2):
		return None

	i1 = 0
	i2 = 0

	while i1 < len(ar1) or i2 < len(ar2):


		if i1 < len(ar1) and i2 < len(ar2):
			
			if ar1[i1] <= ar2[i2]:
				val = ar1[i1]
				i1+=1
			else:
				val = ar2[i2]
				i2+=1

		elif i1 < len(ar1):
			val = ar1[i1]
			i1+=1
		elif i2 < len(ar2):
			val = ar2[i2]
			i2+=1

		if n == i1+i2:
			return val



	# Given a sorted array and a number x, find the pair in array whose sum is closest to x

	# [1,3,4,8,10,15], 6
	# 1+4 = 5, 3+4=7

	# Count total set bits in all numbers from 1 to n

# 1 = 0001 - 1 
# 2 = 0010 - 1 
# 3 = 0011 - 2 
# 4 = 0100 - 1 
# 5 = 0101 - 2 
# 6 = 0110 - 2 
# 7 = 0111 - 3 
# 8 = 1000 - 1 
# 9 = 1001 - 2 
# 10 = 1010 - 2 
# 11 = 1011 - 3 
# 12 = 1100 - 2 
# 13 = 1101 - 3
# 14 = 1110 - 3
# 15 = 1111 - 4


# 14 -> 4-bit
#  7 = 3-bit
# f(14) = f(7) + f(8)+8
# f(n->d digit) =  f(2^(d-1)-1) + f(n - 2^(d-1)-1) + n - 2^(d-1)-1





