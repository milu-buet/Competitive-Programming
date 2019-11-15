


'''
      0 1 2 3 4 5 6 7
pat = A A B X A A A A
lps = 0 1 0 0 1 2 2 2
'''
def LPS2(pat): 
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
	            lps[i] = 0
	            i += 1
	return lps



def KMP(txt, pat):

	lps = LPS2(pat)

	


print(LPS2('ABXAB'))
print(LPS2('ABAB'))
print(LPS2('ABABCABAB'))
print(LPS2('ACAAA'))




