
def nextPerm(L):
	if len(L)<2:
		return L

	pivot = getPivot(L)
	if pivot is None:
		return sorted(L)

	PivotSwapper = getPivotSwapper(L,pivot)
	L[pivot], L[PivotSwapper] = L[PivotSwapper], L[pivot]

	revlist(L,pivot+1,len(L)-1)

	return L



def revlist(L,i,j):
	mid = int((j-i)/2)

	for p in range(i,i+mid+1):
		q = j-(p-i)
		L[p],L[q] = L[q],L[p]


def getPivotSwapper(L,pivot):
	for i in range(len(L))[::-1]:
		if L[pivot] < L[i]:
			return i

	return None


def getPivot(L):
	for i in range(len(L))[::-1]:
		if i-1>=0 and L[i-1]<L[i]:
			return i-1

	return None



a = [1,2]
# c = getPivot(a)
# c = getPivotSwapper(a,0)
# c = revlist(a,1,2)

c = nextPerm(a)
print(c)

# for i in range(6):
# 	c = nextPerm(a)
# 	print(c)