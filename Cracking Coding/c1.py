


#1.3

# O(n^2)
def arbitrary_duplicate(s):
	ui=0
	for i in range(1,len(s)):
		if s[i] not in s[:ui+1]:
			s[ui+1] = s[i]
			ui+=1

	return s[:ui+1]
s = ['a','b','c','e','b','c','f','e']
print(arbitrary_duplicate(s))


# O(n)
def cont_duplicates(s):
	ui=0
	for i in range(1,len(s)):
		if s[i] != s[ui]:
			s[ui+1] = s[i]
			ui+=1

	return s[:ui+1]

s = ['a','a','a','b','b','c']
print(cont_duplicates(s))


