
def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if len(nums) < 3:
        return []
    nums.sort()
    res = set()
    #print(nums[:-2])
    for i, v in enumerate(nums[:-2]):
        #print(i,v)
        if i >= 1 and v == nums[i-1]:
            continue
        d = {}
        for x in nums[i+1:]:
            if x not in d:
                d[-v-x] = 1
            else:
                res.add((v, -v-x, x))
    return res




a = [-1,0,1,2,-1,-4]
b = threeSum(a)
print(b)