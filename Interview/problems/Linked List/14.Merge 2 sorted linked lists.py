



def merge(l1, l2):

	if l1 is None:
		return l2
	elif l2 is None:
		return l1


	head = Node(-1)
	cur = head

	while l1 and l2:

		if l1.val <= l2.val:
			cur.next = l1
			cur = cur.next
			l1 = l1.next

		else:
			cur.next = l2
			cur = cur.next
			l2 = l2.next



	if l1:
		cur.next = l1
	elif l2:
		cur.next = l2

	return head.next
