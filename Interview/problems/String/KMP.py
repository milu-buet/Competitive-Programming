
# search pattern in a string

'''
      0 1 2 3 4 5 6 7
pat = A A B X A A A A
lps = 0 1 0 0 1 2 2 2
'''
# how much first and last match at each pos i
# T(n) = O(n)
# S(n) = O(n)
def LPS(pat): 
	n = len(pat)
	lps = [0]*n
	j=0
	i=1
	while i<n:
	    if pat[i]== pat[j]: 
	        lps[i] = j+1
	        j += 1
	        i += 1
	    else: 
	        if j > 0: 
	            j = lps[j-1] 
	        else: 
	            i += 1
	return lps



# search pat in txt
# T(n) = O(n)
# S(n) = O(n)
def KMP(txt, pat):

	ans = []

	n = len(txt)
	m = len(pat)
	lps = LPS(pat)

	i=0
	j=0
	while i < n:
		if txt[i] == pat[j]:
			i+=1
			j+=1

		if j==m:
			#print("found at", i-m)
			ans.append(i-m)
			j = lps[m-1]
		elif i < n and txt[i] != pat[j]:
			if j>0:
				j = lps[j-1]
			else:
				i+=1

	return ans


	


# print(LPS('ABXAB'))
# print(LPS('ABAB'))
print("lps=",LPS('ABABCABAB'))
# print(LPS('ACAAA'))

print("found positions =",KMP("ABABDABACDABABCABAB", "ABABCABAB"))



def LPS(pat):
	n = len(pat)
	lps = [0]*n

	j=0
	i=1

	while i < n:
		if pat[i] == pat[j]:
			i+=1
			j+=1
			lps[i] = j 

		elif j>0:
			j = lps[j-1]
		else:
			i+=1

	return lps


#search pat in text
def kmp(text, pat):
	lps = LPS(pat)
	n = len(text)
	m = len(pat)
	i=0
	j=0
	
	while i<n:
		if text[i] == text[j]:
			i += 1
			j += 1

		if j==m:
			ans.append(i-m)
			j = lps[m-1]
		elif i<n and text[i] != text[j]:
			if j>0:
				j = lps[j-1]
			else:
				i+=1






