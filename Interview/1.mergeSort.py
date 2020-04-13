# Merge Sort List 
# T(n) = 2*T(n/2) + theta(n) = theta(nlogn)
# S(n) = merge = O(n)
class Solution(object):
    def sortArray(self, nums):  
        n = len(nums)
        if n<=1:
            return nums
        #self.mergesort(nums, 0, n-1)
        #self.mergesortIta(nums)
        #self.sort(nums, 0, n-1)
        self.ita(nums)
        return nums
    
    def mergesort(self, nums, beg, end):
        if beg < end:
            mid = beg + (end-beg)//2
            self.mergesort(nums, beg, mid)
            self.mergesort(nums, mid+1, end)
            self.merge(nums, beg, mid, end)


    def mergesortIta(self, nums):
    	n = len(nums)
    	cs = 1
    	while cs < n:
    		left = 0
    		while left < n-1:
    			mid = min(n-1, left + cs -1)    # mid should not pass the range
    			right = min(n-1, left + 2*cs -1)
    			self.merge(nums, left, mid, right)
    			left += cs*2 
    		cs *= 2

    def merge(self, nums, beg, mid, end):
        temp = []
        i = beg
        j = mid+1
        while i<=mid and j<=end:
            if nums[i] <= nums[j]:
                temp.append(nums[i])
                i+=1
            else:
                temp.append(nums[j])
                j+=1
                
        while i<=mid:
            temp.append(nums[i])
            i+=1
            
        while j<=end:
            temp.append(nums[j])
            j+=1
            
        nums[beg:end+1] = temp




A = [3,2,1,5,6,3,2]
print(Solution().sortArray(A))

# Merge Sort LinkedList 
# T(n) = 2*T(n/2) + theta(n) = theta(nlogn)
# S(n) = O(1)


class Node(object):
	def __init__(self, val):
		self.val = val
		self.next = None

class Solution(object):
    def sortLinkedList(self, node):  
        
        if node is None or node.next is None:
        	return node
        #return self.mergesort(node)
        #return self.mergesortIta(node)
        return self.mergesortIta2(node)

    def mergesort(self, node):
        if node is None or node.next is None:
        	return node
        back,front = self.getbackfront(node)
        node1 = self.mergesort(back)
        node2 = self.mergesort(front)
        return self.merge(node1,node2)

    def getLen(self, node):
    	n = 0
    	while node:
    		node = node.next
    		n+=1
    	return n

    def getnth(self, node, n):
    	n-=1
    	while n and node.next:
    		node = node.next
    		n-=1
    	return node


    def mergesortIta2(self, node):
        n = self.getLen(node)
        cs = 1
        head = node
        while cs < n:
            beg = head
            prevend = None
            while beg:
                mid = self.getnth(beg, cs)
                end = self.getnth(mid, cs+1)
                beg, end, endnxt = self.merge3(beg, mid, end)
                if prevend:
                    prevend.next = beg  #previous tail -> new head
                else:
                    head = beg  # first time
                prevend = end
                beg = endnxt
            cs = 2*cs
        return head

    def merge3(self, beg, mid, end):

        head = Node(None)
        ch = head
        
        h1 = beg 
        h2 = None
        endnxt = None

        if mid:
            h2 = mid.next
            mid.next = None
        
        if end:
            endnxt = end.next
            end.next = None

        while h1 and h2:

            if h1.val <= h2.val:
                ch.next = h1
                ch = ch.next
                h1 = h1.next
            else:
                ch.next = h2
                ch = ch.next
                h2 = h2.next

        while h1:
            ch.next = h1
            ch = ch.next
            h1 = h1.next

        while h2:
            ch.next = h2
            ch = ch.next
            h2 = h2.next


        return head.next, ch, endnxt

    def getbackfront(self, node):
    	
    	fast = node
    	slow = node
    	while fast.next and fast.next.next:
    		fast = fast.next.next
    		slow = slow.next
    	front = slow.next
    	slow.next = None
    	return node,front

    def merge(self, node1, node2):
    	
    	head = Node(None)
    	cur = head

    	while node1 and node2:
    		if node1.val <= node2.val:
    			cur.next  = node1
    			cur = cur.next
    			node1 = node1.next
    		else:
    			cur.next = node2
    			cur = cur.next
    			node2 = node2.next

    	if node1:
    		cur.next  = node1
    	elif node2:
    		cur.next  = node2

    	return head.next

    	return head.next, tail
def show(node):
	while node:
		print(node.val,end=" ")
		node = node.next
	print("")


n1 = Node(3)
n2 = Node(1)
n3 = Node(2)
n4 = Node(1)
n5 = Node(4)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

show(n1)
show(Solution().sortLinkedList(n1))


    




