

def perm(s):

	if len(s) < 2:
		return [s]

	ans = []

	for p in perm(s[1:]):
		for i in range(len(p)):
			ans.append(p[:i]+ s[0] + p[i:])
		ans.append(p + s[0])

	return ans
	#return sorted(ans)


def subset(arr):

	ans = []
	top = 2**(len(arr)) 
	digits = len(bin(top-1)) - 2

	for n in range(top):
		aset = []
		for i in range(digits):
			if (n>>i)&1 == 1:
				aset.append(arr[i])

		ans.append(aset)

	return ans



#print(subset([1,2,3]))
print(perm('abcd'))

