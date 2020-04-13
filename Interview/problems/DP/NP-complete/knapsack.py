# Given,

# Weights = [3,2,1,5,6,8]
# Values =  [3,1,6,2,3,9]
# WeightLimit = 20


####################################################################################################
'''
Determine the max value than can be made with total weight is less than or equal to a given limit.
no repeatation allowed.

i = within first i elements
k = weight limit
f(i,k) = within the first i elements what is the max value with weightlimit k?
f(# of elements, WeightLimit) = Final answer
f(i,k) = max ( f(i-1,k), v[i-1]+f(i-1,k-w[i-1]) )
f(i,0) = 0
f(0,k) = 0
T(n) = O(n*k)
s(n) = O(k)
'''

def dp(w, v, k):

	n = len(w)
	mem = [ [0 for i in range(k+1)] for i in range(2)]

	top = 0
	bottom = 1
	for i in range(1,n+1):
		for j in range(1,k+1):
			mem[bottom][j] = mem[top][j]
			if j >= w[i-1]:
				mem[bottom][j] = max(mem[bottom][j], v[i-1] + mem[top][j-w[i-1]])
		top^=1
		bottom^=1

	return mem[top][-1]

Weights = [3,2,1,5,6,8]
Values =  [3,1,6,2,3,9]
WeightLimit = 20
print(dp(Weights, Values, WeightLimit))

##############################################################################################

'''
Determine the number of each item to include in a collection so that the total weight 
is less than or equal to a given limit and the total value is as large as possible
'''
def dp(w, v, k):

	n = len(w)
	mem = [ [0 for i in range(k+1)] for i in range(n+1)]
	taken = [ [ (0,0) for i in range(k+1)] for i in range(n+1)]


	for i in range(1,n+1):
		for j in range(1,k+1):
			mem[i][j] = mem[i-1][j]
			taken[i][j] = (i-1,j)
			if j >= w[i-1] and mem[i][j] < v[i-1] + mem[i-1][j-w[i-1]]:
				mem[i][j] = v[i-1] + mem[i-1][j-w[i-1]]
				taken[i][j] = (i-1,j-w[i-1])
	i,j = n,k
	ans = []
	while i>0:
		a,b = taken[i][j]
		ans = [int(j!=b)] + ans
		i,j = a,b
	return ans 


Weights = [3,2,1,5,6,8]
Values =  [3,1,6,2,3,9]
WeightLimit = 20
	
print(dp(Weights, Values, WeightLimit))
##############################################################################################
'''
Determine the max value than can be made with total weight is less than or equal to a given limit.
with repeatation allowed.

i = within first i elements
k = weight limit
f(i,k) = within the first i elements what is the max value with weightlimit k?
f(# of elements, WeightLimit) = Final answer
f(i,k) = max ( f(i-1,k), v[i-1]+f(i-1,k-w[i-1]) )
f(i,0) = 0
f(0,k) = 0
T(n) = O(n*k)
s(n) = O(k)

'''# f(k) = max( f(k), v[0]+f(k-w[0]), v[1]+f(k-w[1]), .... )

def dp(w, v, k):
	mem = [0 for i in range(k+1)]
	for i in range(k+1):
		for j in range(len(w)):
			if i >= w[j]:
				mem[i] = max( mem[i], v[j] + mem[i - w[j]])

	return mem[k]

Weights = [3,2,1,5,6,8]
Values =  [3,1,6,2,3,9]
WeightLimit = 20
	
print(dp(Weights, Values, WeightLimit))
##############################################################################################
'''
Determine the number of each item to include in a collection so that the total weight 
is less than or equal to a given limit and the total value is as large as possible 
with repeatation
'''
def dp(w, v, k):
	mem = [0 for i in range(k+1)]
	elems = [[] for i in range(k+1)]
	for i in range(k+1):
		for j in range(len(w)):
			if i >= w[j] and mem[i] < v[j] + mem[i - w[j]]:
				mem[i] = v[j] + mem[i - w[j]]
				elems[i] = elems[i - w[j]] + [j]

	return elems[k]

Weights = [3,2,1,5,6,8]
Values =  [3,1,6,2,3,9]
WeightLimit = 20
	
print(dp(Weights, Values, WeightLimit))