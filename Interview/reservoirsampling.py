#https://www.geeksforgeeks.org/reservoir-sampling/


class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class TreeDiameter:

  def __init__(self):
    self.t = 0

  def find_diameter(self, root):
    # TODO: Write your code here
    self.t = 0
    self.dfs(root)
    return self.t

  def dfs(self, root):
    if root is None:
      return 0

    if root.left:
    	print(root.val, root.left.val)
    
    left = self.find_diameter(root.left)
    print(left)
    right = self.find_diameter(root.right)
    print(right)

    #self.t = max(self.t, left+right+1)
    ret = 1 + max(left, right)
    
    #print(root.val, left, right, ret)
    return ret

def main():
  treeDiameter = TreeDiameter()
  root = TreeNode(1)
  root.left = TreeNode(2)
  # root.right = TreeNode(3)
  # root.left.left = TreeNode(4)
  # root.right.left = TreeNode(5)
  # root.right.right = TreeNode(6)
  print("Tree Diameter: " + str(treeDiameter.find_diameter(root)))
  # root.left.left = None
  # root.right.left.left = TreeNode(7)
  # root.right.left.right = TreeNode(8)
  # root.right.right.left = TreeNode(9)
  # root.right.left.right.left = TreeNode(10)
  # root.right.right.left.left = TreeNode(11)
  # print("Tree Diameter: " + str(treeDiameter.find_diameter(root)))


main()







