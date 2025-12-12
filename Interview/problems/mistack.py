
from collections import deque

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = deque()
        self.min = None
        
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.arr) == 0:
            self.arr.append(x)
            self.min = x
        else:
            self.arr.append(x-self.min)
            if (x < self.min):
                self.min = x

    def pop(self):
        """
        :rtype: None
        """
        ret = self.top()
        top = self.arr.pop()
        
        if top < 0:
            self.min = self.min-top
        return ret

    def top(self):
        """
        :rtype: int
        """
        if len(self.arr)==0:
            return None
        elif len(self.arr) == 1:
            return self.arr[-1]
        elif self.arr[-1] < 0:
            return self.min
        else:
            return self.arr[-1] + self.min

    def getMin(self):
        """
        :rtype: int
        """
        return self.min
        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

obj=MinStack()

obj.push(5)
print(obj.top())
print(obj.pop())
obj.push(5)

obj.push(7)
print(obj.top())
print(obj.pop())
obj.push(7)

obj.push(4)
print(obj.top())
print(obj.pop())
obj.push(4)

obj.push(3)
print(obj.top())
print(obj.pop())
obj.push(3)

obj.push(2)
print(obj.top())
