    

#find equal or closest small
def binSerach1(nums,start,end,val):
	if start > end or end > len(nums)-1:
		return None

	mid = int((start+end)/2)
	#print(start,end,mid)

	if start == end:
		if nums[mid] > val:
			return mid-1
		return mid


	if val == nums[mid]:
		return mid

	elif val < nums[mid]:
		if mid>start:
			return binSerach1(nums,start,mid-1,val)
		elif mid == start:
			return binSerach1(nums,start,mid,val)

	else:
		return binSerach1(nums,mid+1,end,val)



def binSerach3(nums1,start,end,target_med,nums2):
	if start > end:
		return None,None

	mid1 = int((start+end)/2)
	mid2 = binSerach1(nums2,0,len(nums2)-1,nums1[mid1]-0.5)
	mid3 = binSerach1(nums2,0,len(nums2)-1,nums1[mid1])

	#print(mid1,mid2,mid3)


	if mid2 is None or mid2 < 0:
		elem1 = mid1
	else:
		elem1 = mid1+mid2+1


	if mid3 is None or mid3 < 0:
		elem2 = mid1
	else:
		elem2 = mid1+mid3+1

	#print(elem1,elem2)


	if elem1 == target_med:
		return mid1,mid2
	elif elem2 == target_med:
		return mid1,mid3

	elif elem1 > target_med:
		return  binSerach3(nums1,start,mid1-1,target_med,nums2)

	else:
		return binSerach3(nums1,mid1+1,end,target_med,nums2)


def getTargetmid(l):
	return int((l-1)/2)

def getMedianOne(nums1,nums2,target_med):

	mid1,mid2 = binSerach3(nums1,0,len(nums1)-1,target_med,nums2)

	if mid1 is None:
		return None
	
	return float(nums1[mid1])


def getMedian(nums1,nums2):

	l = len(nums1)+len(nums2)
	target_med =  getTargetmid(l)

	c1 = getMedianOne(nums1,nums2,target_med)
	if c1 is None:
		c1 = getMedianOne(nums2,nums1,target_med)

	#print(c1,target_med)
	d1 = getMedianOne(nums1,nums2,target_med+1)
	if d1 is None:
		d1 = getMedianOne(nums2,nums1,target_med+1)
	#print(d1)

	if(l%2==0):
		return (c1+d1)/2

	return c1

a = [1]
b = [1,1,3,3]
c = getMedian(a,b)
#c = binSerach3(a,0,3,4,b)
#c = binSerach1(a,2,3,2.5)

print(c)

