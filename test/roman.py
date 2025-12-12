




def romanToInt(s):
        """
        :type s: str
        :rtype: int
        """

        T1 = ['I','V','X','L','C','D','M']
        V1 = [1,5,10,50,100,500,1000]

        T2 = ['IV','IX','XL','XC','CD','CM']
        V2 = [4,9,40,90,400,900]


        ans=0
        ln=len(s)
        i=0
        while i<ln:
        	if i<ln-1 and s[i:i+2] in T2:
        		ind = T2.index(s[i:i+2])
        		ans = ans + V2[ind]
        		i=i+2
        	elif s[i] in T1:
        		ind = T1.index(s[i])
        		ans = ans + V1[ind]
        		i=i+1
        	print(ans)


       	return ans



s = ""
c = romanToInt(s)
print(c)




