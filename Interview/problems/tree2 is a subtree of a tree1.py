




def eqTree(t1, t2):

	if t1 is None and t2 is None:
		return True
	elif t1 is None or t2 is None:
		return False

	return t1.val == t2.val and eqTree(t1.left, t2.left) and eqTree(t1.right, t2.right)



def isSubtree(t1, t2):

	if t2 is None:
		return True
	elif t1 is None:
		return False

	if eqTree(t1, t2):
		return True

	return isSubtree(t1.left, t2) or isSubtree(t1.right, t2)









