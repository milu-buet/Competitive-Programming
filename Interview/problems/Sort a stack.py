


def sortedInsert(stack, item):
	if len(stack)==0 or item >= stack[-1]:
		stack.append(item)
	else:
		temp = stack.pop()
		sortedInsert(stack, item)
		stack.append(temp)




def sortStack(stack):
	if len(stack) < 2:
		return

	temp = stack.pop()
	sortStack(stack)
	sortedInsert(stack, temp)




s = [1,4,2,3,2]
sortStack(s)

# s = [1,2,3]
# sortedInsert(s, 4)
print(s)




