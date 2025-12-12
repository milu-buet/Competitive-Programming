class Solution:
    def lengthLongestPath(self, S: str) -> int:
        
        #print(input)
        
        
        st=0
        cname = ''
        maxname = -1
        pname = ''

        i=0
        while True:
            
            print('1>')
            if i >= len(S):
                print('2>')
                break
                
            
            if st == 0:
                if S[i]=='\n':
                    st = 1
                    pname = S[:i]
                    i-=1
                else:
                    i+=1
                    print('3>>')
     
            elif st == 1:
                    cname = pname + S[i] + S[i+1]
                    i+=2
                    st=2
            elif st == 2:
                if S[i]=='\n' and S[i+1] == '\t' and S[i+2]!='\t':
                    if '.' in cname:
                        maxname = max(maxname,len(cname))
                        cname = ''
                        st = 1
                    else:
                        cname+=S[i]
                        i+=1
            
            print('4>>>', i, len(S))

        

        return maxname



a = Solution()
S = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
a.lengthLongestPath(S) 