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
                elif nums[mid] < target <= nums[hi]:
                    lo = mid+1
                elif nums[lo] <= nums[mid]:
                    lo = mid+1
                else:
                    hi = mid-1
                    
        if nums[lo] == target:
            return lo
        
        return -1





def bs_l(arr, x):  #== bisect left

    lo = 0
    hi = len(arr)-1


    while lo < hi:
        
        mid = lo + (hi-lo)//2

        if x <= arr[mid]:
            hi = mid
        elif x > arr[mid]:
            lo = mid+1

    return lo


def bs_r(arr, x):  #== bisect right

    lo = 0
    hi = len(arr)-1


    while lo < hi:
        
        mid = lo + (hi-lo)//2

        if x < arr[mid]:
            hi = mid
        elif x >= arr[mid]:
            lo = mid+1

    return lo

def bs_rr(arr, x):  # right most

    lo = 0
    hi = len(arr)-1


    while lo < hi:
        
        mid = lo + (hi-lo)//2

        if x < arr[mid]:
            hi = mid - 1
        elif x >= arr[mid]:
            lo = mid + 1

    return lo


arr = [1,2,2,2,2,2,3,3,4]
print(bs_l(arr,2))

import bisect
print(bisect.bisect_right(arr,2))


            