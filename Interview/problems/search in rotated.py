class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        if len(nums) == 0:
            return -1
        
        lo = 0
        hi = len(nums)-1
        
        while lo < hi:
            mid = (lo+hi)//2
            if target == nums[mid]:
                return mid
            if nums[lo] < nums[hi]:
                # sorted
                if target < nums[mid]:
                    hi = mid-1
                else:
                    lo = mid+1
            else:
                #rotated
                if nums[lo] <= target < nums[mid]:
                    hi = mid-1
                elif nums[lo] <= nums[mid]:
                    lo = mid+1
                elif nums[mid] < target <= nums[hi]:
                    lo = mid+1
                else:
                    hi = mid-1
                    
        if nums[lo] == target:
            return lo
        
        return -1
            