


# f(n) = f(n-1) + f(n-5) + f(n-25)

# n = 100

# 25*0 + ...
# 25*1 + 5*1 + 1*70
# 25*1 + 5*2 + 1*65
# ...
# ...
# 25*4 + 5*0 + 1*00


def ways(n):
	ans = 0
	for i in range(n//25+1):
		v = n - i*25
		for j in range(v//5+1):
			ans+=1
	return ans



print(ways(20))



