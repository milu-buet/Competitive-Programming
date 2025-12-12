
class Queue(object):
	"""docstring for Queue"""
	def __init__(self):
		self.q = []

	def push(self, x):
		self.q.append(x)

	def pop(self):
		self.q.pop(0)

		

q = Queue()
q.push(10) #push
q.push(20)
print(q.q)
q.pop()
print(q.q)



class Stack(object):
	"""docstring for Queue"""
	def __init__(self):
		self.q = []

	def push(self, x):
		self.q.append(x)

	def pop(self):
		self.q.pop(-1)


q = Stack()
q.push(10) #push
q.push(20)
print(q.q)
q.pop()
print(q.q)


 delim = '   \n\t\r'
  words = []
  word = []
  
  delims = []
  dl=[]
  for i in range(len(arr)):
    if arr[i] in delim:
      if len(word)>0:
        words.append(word)
        word=[]
    else:
      word.append(arr[i])
      
    if arr[i] not in delim:
      if len(dl)>0:
        words.append(dl)
        dl=[]
    else:
      dl.append(arr[i])
      
  if len(dl)>0:
        words.append(dl)       
      
  if len(word)>0:
        words.append(word)    
  
  #print(words)
  
  left=0
  right=len(words)-1
  
  while left<len(words) and right>=0 and left<right:
    if words[left][0] not in delim and words[right][0] not in delim:
      words[left],words[right] = words[right],words[left]
      left+=1
      right-=1
    
    if words[left][0] in delim:
      left+=1
      
    if words[right][0] in delim:
      right-=1
      
  
  #print(words)
  sm=[]
  for word in words:
    sm=sm+word
  
  return sm
      