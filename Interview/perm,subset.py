

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        out = []
        self.perm(nums, 0, out)
        
        return out
        
    
    def perm(self, nums, i, out):
        if i>= len(nums):
            out.append(list(nums))
            
        for k in range(i, len(nums)):
            nums[i],nums[k] = nums[k],nums[i]
            self.perm(nums, i+1, out)
            nums[i],nums[k] = nums[k],nums[i]




def subset(arr):

	ans = []
	top = 2**(len(arr)) 
	digits = len(bin(top-1)) - 2

	for n in range(top):
		aset = []
		for i in range(digits):
			if (n>>i)&1 == 1:
				aset.append(arr[i])

		ans.append(aset)

	return ans



#print(subset([1,2,3]))
print(Solution().permute(['a','b','c']))




