class Solution:
    def findDuplicate(self, nums):
        # Find the intersection point of the two runners.
        tortoise = nums[0]
        hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
        
        # Find the "entrance" to the cycle.
        ptr1 = nums[0]
        ptr2 = tortoise
        while ptr1 != ptr2:
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]
        
        return ptr1







 l = len(nums1)+len(nums2)
        
        if l==0:
            return 0.0
        
        target_med =  self.getTargetmid(l)

        c1 = self.getMedianOne(nums1,nums2,target_med)
        if c1 is None:
            c1 = self.getMedianOne(nums2,nums1,target_med)


        d1 = self.getMedianOne(nums1,nums2,target_med+1)
        if d1 is None:
            d1 = self.getMedianOne(nums2,nums1,target_med+1)

        if(l%2==0):
            return (c1+d1)/2

        return c1
            
        
        return c1
        
    #find equal or closest small
    def binSerach1(self,nums,start,end,val):
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
                return self.binSerach1(nums,start,mid-1,val)
            elif mid == start:
                return self.binSerach1(nums,start,mid,val)

        else:
            return self.binSerach1(nums,mid+1,end,val)



    def binSerach3(self,nums1,start,end,target_med,nums2):
        if start > end:
            return None,None

        mid1 = int((start+end)/2)
        mid2 = self.binSerach1(nums2,0,len(nums2)-1,nums1[mid1]-0.5)
        mid3 = self.binSerach1(nums2,0,len(nums2)-1,nums1[mid1])


        if mid2 is None or mid2 < 0:
            elem1 = mid1
        else:
            elem1 = mid1+mid2+1


        if mid3 is None or mid3 < 0:
            elem2 = mid1
        else:
            elem2 = mid1+mid3+1


        if elem1 == target_med:
            return mid1,mid2
        elif elem2 == target_med:
            return mid1,mid3

        elif elem1 > target_med:
            return  self.binSerach3(nums1,start,mid1-1,target_med,nums2)

        else:
            return self.binSerach3(nums1,mid1+1,end,target_med,nums2)


    def getTargetmid(self,l):
        return int((l-1)/2)

    def getMedianOne(self,nums1,nums2,target_med):

        mid1,mid2 = self.binSerach3(nums1,0,len(nums1)-1,target_med,nums2)

        if mid1 is None:
            return None

        return float(nums1[mid1])