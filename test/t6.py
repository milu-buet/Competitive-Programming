
def binSerach(nums,start,end,val):
	if start > end:
		return start

	mid = (start+end)//2

	if val == nums[mid]:
		return mid

	elif val < nums[mid]:
		return binSerach(nums,start,mid-1,val)

	else:
		return binSerach(nums,mid+1,end,val)



def binSerach2(nums,start,end,val):
	if start > end:
		return end

	mid = int((start+end)/2)

	if val == nums[mid]:
		return mid

	elif val < nums[mid]:
		return binSerach2(nums,start,mid-1,val)

	else:
		return binSerach2(nums,mid+1,end,val)




nums = [1,3,5,7,9,11]
val = 10

r2 = binSerach(nums,0,len(nums)-1,val)
r1 = binSerach2(nums,0,len(nums)-1,val)
print(nums[r1],nums[r2])