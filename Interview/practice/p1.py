
def quicksort(nums, beg, end):
	if beg < end:
		pi = partition(nums, beg, end)
		quicksort(nums, beg, pi-1)
		quicksort(nums, pi+1, end)

def quickselect(nums, beg, end, k):
	pi = partition(nums, beg, end)
	n = pi-beg+1

	if k == n:
		return nums[k]
	elif k < n:
		return quickselect(nums, beg, pi-1, k)
	elif k > n:
		return quickselect(nums, pi+1, end, k-n)

import random
def partition(nums, beg, end):
	pv = random.randint(beg, end)
	nums[pv], nums[end] = nums[end], nums[pv]

	left = beg
	for i in range(beg, end):
		if nums[i] < nums[end]:
			nums[i], nums[left] = nums[left], nums[i]
			left +=1
	nums[left], nums[end] = nums[end], nums[left]
	return left



a = [2,5,1,2,3,1,-1]
quicksort(a, 0 , len(a)-1)
print(a)
