
# searching pattern
# searching Duplicate Substring




# https://www.youtube.com/watch?v=oxd_Z1osgCk
'''
***Using hash value to search a string***

1. convert the while sting to humber:
    S = 'dcba' => 3 2 1 0

2. make own hash of a subtring: 'dcba'
    h = 3*26^3 + 2*26^2 + 1*26^1 + 0*26^0

3. use set/hashmap to find duplicats based on h

4. hash collision might be a problem

'''





# Longest Duplicate Substring

from collections import defaultdict
class Solution:
    def longestDupSubstring(self, S: str) -> str:
        
        nS = []
        for c in S:
            nS.append(ord(c)-ord('a'))
        
        MOD = 2**32
        n=len(S)
        lo = 1
        hi = n-1
        ans = ''
        j=None
        midj = None
        while lo <= hi:
            mid = lo + (hi-lo)//2
            i = self.check(mid, nS, MOD)
            
            if i>-1:
                lo = mid + 1
                j=i
                midj = mid
                    
            else:
                hi = mid-1
        
        if midj:
            return S[j:j+midj]
        return ""
    
    
    def check(self, m, S, MOD):
        
        h = 0
        for i in range(m):
            h = ( h*26 + S[i] ) % MOD
            
        dp = set([h])
        aL = 26**m % MOD
        for i in range(1, len(S)-m+1):  # 01234 5-2=3
            
            h =  ( h*26 - S[i-1]*aL + S[i+m-1] ) %MOD
            
            if h in dp:
                return i
            else:
                dp.add(h)  
        
        return -1

        

print(Solution().longestDupSubstring("banana"))