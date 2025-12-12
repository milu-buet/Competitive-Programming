import bisect
class Solution:
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        dp = [0] * len(nums)
        size = 0
        for n in nums:
            idx = bisect.bisect_left(dp, n, 0, size)
            #print(idx, dp)
            dp[idx] = n
            if idx == size:
                size += 1
        return size

    def getLIS(self, nums):
        dp = [0]*len(nums)
        dp[-1] = 1

        ne = [None]*len(nums)


        for i in range(len(nums)-2,-1,-1):
            for j in range(i+1,len(nums)):
                if nums[i] < nums[j] and dp[i] < 1 + dp[j]:
                    dp[i] = 1 + dp[j]
                    ne[i] = j
        
        #print(ne)
        i_max = dp.index(max(dp))
        ans = [nums[i_max]]
        i = i_max
        while ne[i] is not None:
            ans.append(nums[ne[i]])
            i = ne[i]

        return ans
        

        #print(dp, ne)




A = [5,1,10,3,2,9,3,7,4]
print(A)
print(Solution().lengthOfLIS(A))
print(Solution().getLIS(A))