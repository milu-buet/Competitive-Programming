'''
https://en.wikipedia.org/wiki/Fenwick_tree
https://www.topcoder.com/community/data-science/data-science-tutorials/binary-indexed-trees/

LSB(i) = i & (-i))
LSB(20) = LSB(10100) = 100 = 4

'''
class BIT:

    def __init__(self, nums):
        
        self.n = len(nums)
        self.nums = nums
        self.bit = [0]*(self.n+1)
        
        for i, val in enumerate(nums):
            self.update_diff(i, val)
            
    def update(self, i, val) -> None:
        diff = val - self.nums[i]
        self.nums[i] = val
        self.update_diff(i, diff)
    
    def update_diff(self, i, diff):
        i += 1
        while i <= self.n:
            self.bit[i] += diff
            i += (i & (-i))
            
    def getsum(self, i):
        i += 1
        sm = 0
        while i>0:
            sm += self.bit[i]
            i -= (i & (-i))
        return sm
        
    def sumRange(self, i, j):
            return self.getsum(j) - self.getsum(i-1)


arr = [1,5,1,7,8,9]
bit = BIT(arr)
print(bit.sumRange(2,4))
bit.update(2, 3) # 1->3
print(bit.sumRange(2,4))


