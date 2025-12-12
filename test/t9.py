
import math
class Solution:
    def kMirror(self, k: int, n: int) -> int:
        
        
        def check(num, k):
            nm = num
            s = ''
            p = int(math.log(nm, k))
            #print(p)
            while p > -1:
                d = nm//(k**p)
                nm = max(0, nm - d*(k**p))
                p -= 1
                
                #print(nm, d, p)
                s += str(d)
            
            #print(">>", num, s)
            return s == s[::-1]
    
    
        #print(check(29092, 3))
            
            
        c = 0
        ans = 0
        for d in range(1,16):
            if d==1:
                for num in range(1,10):
                    if check(num, k):
                        print(num, c, n)
                        c+=1
                        ans += num
                        if c==n:
                            return ans
            else:
                hd = d//2
                for s in range(10**(hd-1), 10**(hd)):
                    if d%2==0:
                        num = s*10**(hd) + int(str(s)[::-1])
                        if check(num, k):
                            print(num, c, n)
                            c+=1
                            ans += num
                            if c==n:
                                return ans
                                
                    else:
                        for mid in range(0,10):
                            num = s*10**(hd+1) + mid*10**hd + int(str(s)[::-1])
                            if check(num, k):
                                print(num, c, n)
                                c+=1
                                ans += num
                                if c==n:
                                    return ans
        
                

Solution().kMirror(4, 30)