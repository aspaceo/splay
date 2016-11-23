# python3

from sys import stdin

# Splay tree implementation

# Vertex of a splay tree
class Vertex:
  def __init__(self, key, sum, left, right, parent):
    (self.key, self.sum, self.left, self.right, self.parent) = (key, sum, left, right, parent)

  def hasLeftChild(self):
    return self.left is not None

  def hasRightChild(self):
    return self.right is not None

  def hasBothChildren(self):
    return(self.hasLeftChild and self.hasRightChild)

  def isLeaf(self):
    if (self.hasLeftChild() or self.hasRightChild()):
      return False
    else:
      return True

  def hasAnyChildren(self):
    return self.right or self.left

  def isLeftChild(self):
    return self.parent and self.parent.left.key == self.key

  def isRightChild(self):
    return self.parent and self.parent.right.key == self.key

  def isRoot(self):
    return self.parent is None

  def findMin(self):
    current = self
    while current.hasLeftChild():
      current = current.left
    return current

  def findSuccsessor(self):
    succ = None
    if self.hasRightChild():
      succ = self.right.findMin()
    else:
      if self.parent:
        if self.isLeftChild():
          succ = self.parent
        else:
          self.parent.right = None
          succ = self.parent.findSuccessor()
          self.parent.right = self
    return succ


  def replaceNodeData(self, key, sum, lc, rc):
    self.key = key
    self.sum = sum
    self.left = lc
    self.right = rc
    if self.hasLeftChild():
      self.left.parent = self
    if self.hasRightChild():
      self.right.parent = self

  def spliceOut(self):
    if self.isLeaf():
      if self.isLeftChild():
        self.parent.left = None
      else:
        self.parent.rightChild = None
    elif self.hasAnyChildren():
      if self.hasLeftChild():
        if self.isLeftChild():
          self.parent.left = self.left
        else:
          self.parent.right = self.left
        self.left.parent = self.parent
      else:
        if self.isLeftChild():
          self.parent.left = self.right
        else:
          if self.isLeftChild():
            self.parent.left = self.right
          else:
            self.parent.right = self.right
          self.right.parent = self.parent

def update(v):
  if v == None:
    return
  v.sum = v.key + (v.left.sum if v.left != None else 0) + (v.right.sum if v.right != None else 0)
  if v.left != None:
    v.left.parent = v
  if v.right != None:
    v.right.parent = v

def smallRotation(v):
  parent = v.parent
  if parent == None:
    return
  grandparent = v.parent.parent
  if parent.left == v:
    m = v.right
    v.right = parent
    parent.left = m
  else:
    m = v.left
    v.left = parent
    parent.right = m
  update(parent)
  update(v)
  v.parent = grandparent
  if grandparent != None:
    if grandparent.left == parent:
      grandparent.left = v
    else: 
      grandparent.right = v

def bigRotation(v):
  if v.parent.left == v and v.parent.parent.left == v.parent:
    # Zig-zig
    smallRotation(v.parent)
    smallRotation(v)
  elif v.parent.right == v and v.parent.parent.right == v.parent:
    # Zig-zig
    smallRotation(v.parent)
    smallRotation(v)    
  else: 
    # Zig-zag
    smallRotation(v);
    smallRotation(v);

# Makes splay of the given vertex and makes
# it the new root.
def splay(v):
  if v == None:
    return None
  while v.parent != None:
    if v.parent.parent == None:
      smallRotation(v)
      break
    bigRotation(v)
  return v

# Searches for the given key in the tree with the given root
# and calls splay for the deepest visited node after that.
# Returns pair of the result and the new root.
# If found, result is a pointer to the node with the given key.
# Otherwise, result is a pointer to the node with the smallest
# bigger key (next value in the order).
# If the key is bigger than all keys in the tree,
# then result is None.
def find(root, key): 
  v = root
  last = root
  next = None
  while v != None:
    if v.key >= key and (next == None or v.key < next.key):
      next = v    
    last = v
    if v.key == key:
      break    
    if v.key < key:
      v = v.right
    else: 
      v = v.left      
  root = splay(last)
  return (next, root)

def split(root, key):  
  (result, root) = find(root, key)  
  if result == None:    
    return (root, None)  
  right = splay(result)
  left = right.left
  right.left = None
  if left != None:
    left.parent = None
  update(left)
  update(right)
  return (left, right)

  
def merge(left, right):
  if left == None:
    return right
  if right == None:
    return left
  while right.left != None:
    right = right.left
  right = splay(right)
  right.left = left
  update(right)
  return right

  
# Code that uses splay tree to solve the problem
                                    
root = None

def insert(x):
  global root
  (left, right) = split(root, x)
  new_vertex = None
  if right == None or right.key != x:
    new_vertex = Vertex(x, x, None, None, None)  
  root = merge(merge(left, new_vertex), right)
  
def erase(tree_root, x):
  global root
  # Implement erase yourself  -------------------------------------------------
  if tree_root.key == x:
    remove(tree_root, x)
  elif tree_root.key > x and tree_root.hasLeftChild():
    erase(tree_root.left, x)
  elif tree_root.hasRightChild():
    erase(tree_root.right, x)

def remove(root, x):
  if root.isRoot():
    root = None
  elif root.isLeaf():  ## node is a leaf  ---------------------------------------
    if root.parent.left == root:
      root.parent.left = None
    else:
      root.parent.right = None
  elif root.hasBothChildren():  ## has two children  --------------------------
    succ = root.findSuccessor()
    succ.splicedOut()
    ## update vertex values  --------------------------------------------------
    root.key = succ.key
  else: ## has one child  -----------------------------------------------------
    if root.hasLeftChild():
      if root.isLeftChild():
        root.left.parent = root.parent
        root.parent.left = root.left
      elif root.isRightChild():
        root.left.parent = root.parent
        root.parent.left = root.left
      else:
        root.replaceNodeData(root.left.key
                             , root.left.sum
                             , root.left.left
                             , root.left.right
                             )
    else:
      if root.isLeftChild():
        root.right.parent = root.parent
        root.parent.left = root.left
      elif root.isRightChild():
        root.right.parent = root.parent
        root.parent.right = root.right
      else:
        root.replaceNodeData(root.right.key
                             , root.right.sum
                             , root.right.left
                             , root.right.right
                             )

# def search(x):
#   global root
#   # Implement find yourself
#
#   return False
#
# def sum(fr, to):
#   global root
#   (left, middle) = split(root, fr)
#   (middle, right) = split(middle, to + 1)
#   ans = 0
#   # Complete the implementation of sum
#
#   return ans
#
# MODULO = 1000000001
# n = int(stdin.readline())
# last_sum_result = 0
# for i in range(n):
#   line = stdin.readline().split()
#   if line[0] == '+':
#     x = int(line[1])
#     insert((x + last_sum_result) % MODULO)
#   elif line[0] == '-':
#     x = int(line[1])
#     erase((x + last_sum_result) % MODULO)
#   elif line[0] == '?':
#     x = int(line[1])
#     print('Found' if search((x + last_sum_result) % MODULO) else 'Not found')
#   elif line[0] == 's':
#     l = int(line[1])
#     r = int(line[2])
#     res = sum((l + last_sum_result) % MODULO, (r + last_sum_result) % MODULO)
#     print(res)
#     last_sum_result = res % MODULO