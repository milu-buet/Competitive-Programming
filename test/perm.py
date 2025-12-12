

def pm(n):

	if n <= 0:
		return 0

	if n <= 2:
		return 1

	return (n-1)*fact(n)*(pm(n-2) + (n-2)*pm(n-3))//2


def fact(n):
	if n<=1:
		return 1

	ml = 1
	for i in range(1,n+1):
		ml*=i

	return ml



# for i in range(1,100):
# 	print(pm(i))





def f(n):

	if n==1:
		return 10


	return (perm(10,n) - perm(9,n-1)) + f(n-1)

def perm(n,r):

	return fact(n)//fact(n-r)


def fact(n):
	if n<=1:
		return 1

	ml = 1
	for i in range(1,n+1):
		ml*=i

	return ml


#ans = {1:10, 2:91, 3:739, 4:5275, 5:32491, 6:168571, 7:712891, 8:2345851, 9:5611771}
#print(f(10))
for i in range(1,12):
	print(i, f(i))
