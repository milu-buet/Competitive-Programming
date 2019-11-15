
class Node(object):
	"""docstring for Node"""
	def __init__(self, val):
		self.val = val
		self.next = None

# 1->2->3->null
# a=None, b=1
# 1 2->3->null
# a=1 b=2
# 1<-2 3->null
# a=2, b=3
def rev(head):

	a = None
	b = head

	while b:
		c = b.next
		b.next = a

		a = b
		b = c

	return a





n1 = Node(1)
n2 = Node(2)
n3 = Node(3)

n1.next = n2
n2.next = n3

n1 = rev(n1)
print(n1.next.next.val)







