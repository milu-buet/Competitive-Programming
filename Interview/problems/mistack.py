

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []
        self.min = None
        
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.arr == 0):
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
        top = self.arr.pop(-1)
        if top < 0:
            self.min = self.min-top

    def top(self):
        """
        :rtype: int
        """
        if len(self.arr == 1):
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