# Quick Sort List 
# T(n): theta(n) + T(k) + T(n-k-1) = worst: O(n^2), avg: O(nlogn)
# S(n) = O(1)
class Solution(object):
    def sortArray(self, nums):  
        n = len(nums)
        if n<=1:
            return nums
        #self.quicksort(nums, 0, n-1)
        self.quicksortIta(nums)
        return nums

    def quicksort(self, nums, beg, end):
        if beg < end:
            pi = self.partition(nums, beg, end)
            self.quicksort(nums, beg, pi-1)
            self.quicksort(nums, pi+1, end)

    def quicksortIta(self, nums):
        stack = [(0,len(nums)-1)]
        while stack:
            beg, end = stack.pop()
            if beg >= end:
                continue
            pi = self.partition(nums, beg, end)
            stack.append((pi+1,end))
            stack.append((beg,pi-1)) 

    def partition(self, nums, beg, end):
        pi = end
        pivot  = nums[pi]
        nums[end],nums[pi] = nums[pi], nums[end]
        i = beg-1 # how many elements ae smaller
        for j in range(beg,end):
            if nums[j] < pivot:
                i+=1
                nums[i],nums[j] = nums[j],nums[i]
        nums[i+1],nums[end] = nums[end],nums[i+1]
        return i+1




A = [3,2,1,5,6,3,2]
print(Solution().sortArray(A))

