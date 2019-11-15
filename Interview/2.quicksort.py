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

#
    def quicksortIta(self, nums):
        stack = [(0,len(nums)-1)]
        while stack:
            beg, end = stack.pop()
            if beg >= end:
                continue
            pi = self.partition(nums, beg, end)
            stack.append((pi+1,end))
            stack.append((beg,pi-1)) 

# T(n) = n + T(n-p)
# # best: p=n/2
# T(n) = n + T(n/2) = n + n/2 + n/4 .... = O(2n)
# T(n) = n + T(n-1) = n + n-1 + .... =  O(n^2) 

# S(n) = O(1)
    def quickselect(self, nums, beg, end, k):  # find kth smallest element
        
        pi = self.randpartition(nums, beg, end)
        if pi-beg == k-1:
            return nums[pi]
        elif pi-beg > k-1:
            return self.quickselect(nums, beg, pi-1, k)
        else:
            return self.quickselect(nums, pi+1, end, k-1 -pi+beg)


    def qkita(self, nums, k):

        beg = 0
        end = len(nums)-1

        while beg < end:
            pi = self.randpartition(nums, beg, end)
            if pi-beg == k-1:
                return nums[pi]
            elif pi-beg > k-1:
                end = pi-1
            else:
                beg = pi+1
                k = k-(pi-beg+1)

        if k==1:
            return nums[lo]

        return None


    def randpartition(self, nums, beg, end):

        import random
        pi = random.randint(beg, end)
        nums[pi],nums[end] = nums[end],nums[pi]
        return self.partition(nums, beg, end)

    def partition(self, nums, beg, end):
        pi = end
        pivot  = nums[pi]
        i = beg-1 # how many elements ae smaller
        for j in range(beg,end):
            if nums[j] < pivot:
                i+=1
                nums[i],nums[j] = nums[j],nums[i]
        nums[i+1],nums[end] = nums[end],nums[i+1]
        return i+1



A = [3,2,1,5,6,3,2]
#Solution().sort(A,0,len(A)-1)
Solution().sortIta(A)
print(A)

