

# 	 z
#   / \
#  y   T3
# / \
#T1  T2

#   y
#  / \
# T1  z
#    / \
#   T2  T3

def rorate_right(root):

	z = root
	y = root.left

	z.left = y.right
	y.right = z

	y.height = 1 + max(getheight(y.left), getheight(y.right))
	z.height = 1 + max( getheight(z.left), getheight(z.right))

def getheight(node):
	if node:
		return node.height
	return 0

