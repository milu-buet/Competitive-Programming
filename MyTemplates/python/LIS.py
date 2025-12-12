

import bisect

def lengthOfLIS(nums):
    # consider the longest increasing subsequence
    if len(nums) <= 1: 
    	return len(nums)

    n = len(nums)
    lis = [0]*n
    p = 1
    lis[0] = nums[0]
    for i in range(1, n):
        print(p, nums[i], lis)
        if nums[i] > lis[p-1]:
            lis[p] = nums[i]
            p += 1
        elif nums[i] < lis[0]:
            lis[0] = nums[i]
        else:
            # our value is somewhere in the midddle, find the location
            j = bisect.bisect_left(lis, nums[i], 0, p)
            # if the value actually exists in our array, do nothing
            if lis[j] != nums[i]:
                # the leading element of lis[j] will now be smaller than it was before
                lis[j] = nums[i]
    return p



a = [10,9,2,5,3,7,101,18]
print(lengthOfLIS(a))