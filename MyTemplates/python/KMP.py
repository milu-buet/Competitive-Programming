




def LPS(pat):
	ans = [0,]

	left=0

	for right in range(1,len(pat)):
		if pat[left] == pat[right]:
			ans.append(left+1)
		else:
			while left>0 and pat[left] != pat[right]:
				left = ans[left-1]

			if pat[left] == pat[right]:
				ans.append(left+1)
			else:
				ans.append(left)

		left+=1

	return ans





txt = "ABABABCABABABCABABABC"
pat =  "ABABCABAB"

print(LPS(pat))

