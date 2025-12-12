'''
Decreasing queue: 10 5 1
# the left most is the highest in the current range

# 10 5 1
#    j i
# j+1 --- i-1 are smaller than i



Increasing queue: 1 5 10
The left most is the smallest in the current range 

# 1 5 10
#    j i
# j+1 --- i-1 are higher than i

'''



from collections import deque
class Solution:
    def maxSlidingWindow(self, nums, k):

# Checking for base case
        if not nums:
            return []
        if k == 0:
            return nums
# Defining Deque and result list
        deq = deque()
        result = []

        for i in range(k):
            while len(deq) > 0 and nums[deq[-1]] < nums[i]:
                deq.pop()
            deq.append(i)

        print(deq)

 
        for i in range(k, len(nums)):
            result.append(nums[deq[0]])
            
            if deq[0] < i - k + 1:
                deq.popleft()
            
            while len(deq) > 0 and nums[deq[-1]] < nums[i]:
                deq.pop()
            deq.append(i)
        
#Adding the maximum for last subsequence
        result.append(nums[deq[0]])
        
        return result


nums = [1,3,-1,-3,0,3,6,7]
k=3
res = Solution().maxSlidingWindow(nums, k)
print(res)


