

class Node(object):
	"""docstring for Node"""
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None





class PrettyPrint(object):
	"""docstring for PrettyPrint"""
	def __init__(self, root):
		self.root = root


	def getHeight(self, root):
		if root is None:
			return 0

		leftH = self.getHeight(root.left)
		rightH = self.getHeight(root.right)

		return 1 + max(leftH, rightH)


	def print(self):

		q = [self.root]
		level = 1
		height = self.getHeight(self.root)
		#print(height)

		while q:
			#print(height-level)
			i = height - level
			self.spaces(self.nodestartSpace(i))
			nq = []
			while q:
				node = q.pop(0)
				
				print(node.val, end="")

				v = self.nodeSpace(i)
				self.spaces(v)

				if node.left:
					nq.append(node.left)

				if node.right:
					nq.append(node.right)
			

			if i>0:
				print("")
				self.spaces(self.slashtartSpace(i))
				inner = self.slashinnerSpace(i)
				outer = self.slashouterSpace(i)
				#print(outer)
				#print('/',end = '')

				for j in range(level):
					print('/',end='')
					self.spaces(inner)
					print("\\",end='')
					self.spaces(outer)







			print("")
			q = nq
			level += 1

		#print(level)


	def spaces(self, n):
		print(" "*n, end="")



	def nodestartSpace(self, i):
		pass

		# f(l=h) = 0
		# f(l=h-1) = 2
		# f(l=h-2) = 6
		# f(l=h-3) = 14
		# 0, 2, 6, 14, 
		# 0, 0+2, 2+4, 6+8

		# f(0) = 0
		# f(i) = f(i-1) + 2^i
		# i = h-l

		if i==0:
			return 0

		return self.nodestartSpace(i-1) + 2**i




	def nodeSpace(self, i):
		pass

		# 3, 7, 15
		# 3, 3+4, 7+8

		# f(0) = 3
		# f(i) = f(i-1) + 2^(i+1)

		if i==0:
			return 3

		return self.nodeSpace(i-1) + 2**(i+1)




	def slashtartSpace(self, i):
		pass

		# 1, 3, 7

		# f(1) = 1
		# f(i) = f(i-1) + 2**(i-1) 

		if i==1:
			return 1

		return self.slashtartSpace(i-1) + 2**(i-1)


	def slashinnerSpace(self, i):
		pass

		# 1, 5, 13

		# f(1) = 1
		# f(i) = f(i-1) + 2**(i) 


		if i==1:
			return 1

		return self.slashtartSpace(i-1) + 2**(i)


	def slashouterSpace(self, i):
		# 5, 9, 13

		if i==1:
			return 5

		return self.slashouterSpace(i-1) + 4





n1 = Node(1)

n2 = Node(2)
n3 = Node(3)

n1.left = n2
n1.right = n3

n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)

n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7



PrettyPrint(n1).print()



'''

--------------x
-------/-------------\
------x---------------x
---/-----\---------/-----\
--x-------x-------x-------x
-/-\-----/-\-----/-\-----/-\
x---x---x---x---x---x---x---x

'''

#HF034SRV

		

		