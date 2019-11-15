import bisect
class Solution:
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        dp = [0] * len(nums)
        size = 0
        for n in nums:
            idx = bisect.bisect_left(dp, n, 0, size)
            #print(idx)
            dp[idx] = n
            if idx == size:
                size += 1
        return size



A = [5,1,10,3,2,9,3,7,4]
print(Solution().lengthOfLIS(A))