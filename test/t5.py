# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return head
        
        A=None
        B=head
        head,last = self.reverse_all(A,B,k)

        show(head)
        print('>>')
        
        while(last.next is not None):
                A=last
                B=last.next
                print(A.val,B.val)
                first,last = self.reverse_all(A,B,k)
        
        return head

    
    def reverse_all(self,A,B,k):
        
        if k==1:
            return B,B
       
        if k==2:
            if B.next is not None:
                C = self.rev2(A,B,B.next)
                return C,B
            else: return B,B
        else:
            C = self.getKthBefore(B,k)
            if C is None:
                return B,B   
            D = C.next
            if D is None:
                return B,B
            D = self.revk(A,B,C,D)
        
        A = D
        B = D.next
        self.reverse_all(A,B,k-2)
            
        return D,C.next
        
    def getKthBefore(self,head,k):
        
        if k == 1:
            return None
        if k == 2:
            return head
        
        while(k-2>0 and head is not None):
            head = head.next
            k-=1
        
        return head
    
    def rev2(self,A,B,C):   #swap B,C in A->B->C
        #print(A,B.val,C.val)
        
        if A is not None:
            A.next = C
        B.next = C.next
        C.next = B 
            
        return C

                 
    def revk(self,A,B,C,D): #swap B,D in A->B-> ..... ->C->D
        if A is not None:
            A.next = D
        
        t1 = B.next
        B.next = D.next
        C.next = B
        D.next = t1
        
        return D


def show(head):
	t=0
	while(head is not None):
		print(t,head.val)
		head=head.next
		t=t+1
		#break
        


a = [1,7,3,2,7,0,1,0,0]
head = ListNode(a[0])
prev = head
for x in a[1:]:
	node = ListNode(x)
	prev.next = node
	prev = node


obj = Solution()
#head = obj.getKthBefore(head,5)
#print(head.val)


# A=None
# B=head
# C=head.next
# head = obj.rev2(A,B,C)

head = obj.reverseKGroup(head,4)

print(">>>")
show(head)

