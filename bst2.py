from sys import stdin

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    '''
        the put method checks to see if the tree already has a root
        if not then put will create a new TreeNode and install it as the root of the tree
        if the root is already in place, put will call the private, recursive helper
        function _put to search the tree according to the following algorithm:

        - starting as the root of the tree, search the binary tree comparing the new
            key to the current node key. if new key is more, search the right subtree
            else left subtree
        - when there is no left (or right) child to search, we have found the position
            in the tree where the new node should go
        - to add a node to the tree, create a new TreeNode object and insert the object
            as the point discoved in the previous step

    '''

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size = self.size + 1

    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent = currentNode)
        elif key > currentNode.key:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent = currentNode)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self, key, currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key, currentNode.leftChild)
        else:
            return self._get(key, currentNode.rightChild)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False



    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
    def _get(self, key, currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key, currentNode.leftChild)
        else:
            return self._get(key, currentNode.rightChild)

    '''
        Using get we can implement the in operation by writing a __contains__ method
        for the tree.

    '''

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False

    '''
        finally we turn our attention to the most challenging method in the search tree,
        the deletion of a key.
            - the first task is to find the node to delete by searching the tree
            - if the key is not found the del operator raises an error

    '''

    def delete(self, key):
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size - 1
            else:
                raise KeyError('Error, key not in tree')
    '''
        once we've found the node containing the key we want to delete, there are three
        cases we must consider
            - the node to be deleted has no children
            - the node to be deleted has only one chile
            - the node to be deleted has two children
    '''

    def __delitem__(self, key):
        self.delete(key)

    def remove(self, currentNode):
        if currentNode.isLeaf():  ## leaf  ------------------------------------
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
            # the third case is the most difficult to handle; if a node has two children
            # it is unlikely we can simply promote one of them to take the nodes place.
            # instead, we can search the tree for a node that can be used to replace the
            # one scheduled for deletion. What we need is a node that will preserve the bst
            # relationships for both of the existing left and right subtrees. The node that
            # will do this is the node with the next largest key in the tree. We call this
            # the successor. The successor is guaranteed to have no more than one child,
            # so we know how to remove it already.
        elif currentNode.hasBothChildren():  ## two children  -----------------
            succ = currentNode.findSuccessor()
            succ.splicedOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload
            # the second case is only slightly more complicated. If a node has only a single
            # child, then we can simply promote the child to take the place of its parent.
            #
            # There are six cases to consider, since the cases are symmetric with respect to either
            # having a left or right child, we will just discuss the case where the current node
            # has a left child. The decision proceeds as follows:
            #
            # - if the current node is a left child then we only need to update the parent
            #     reference of the parent of the current node, then update the left child
            #     reference of the parent to point to the current nodes left child
            # - if the current node is a right child, we only need to update the parent
            #     reference of the left child to point to the parent of the current node,
            #     and then update the right child reference of the parent to point
            #     to the current node's left child
            # - if the current node has no parent, it must be the root. In this case we will
            #     just replace the key, payload, leftChild, and rightChild data by calling
            #     replaceNodeData method on the root
        else:  ##  node has one child  ----------------------------------------
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else:
                    currentNode.replaceNodeData(currentNode.leftChild.key
                                                , currentNode.leftChild.payload
                                                , currentNode.leftChild.leftChild
                                                , currentNode.leftChild.rightChild)
            else:
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:
                    currentNode.replaceNodeData(currentNode.rightChild.key
                                                , currentNode.rightChild.payload
                                                , currentNode.rightChild.leftChild
                                                , currentNode.rightChild.rightChild)

    def sum(self, low, high):
        current_sum = 0
        for node in range(low, high + 1):
            if node in self:
                current_sum += node
        return(current_sum)



class TreeNode:
    ''' - TreeNode provides many helper functions to BinarySearchTree
        - many of these helper functions help to classify a node according
            to its own position as a child and the kind of children it has
    '''

    def __init__(self, key, val, left = None, right = None, parent = None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild
    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self
    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

    '''
        find successor makes use of the same properties of bst's that cause in order
        traversal to print out the nodes in the tree from the smallest to largest.

        there are three cases to consider when looking for a successor:

            - if the node has a right child, then the successor is the smallest key
                in the right subtree
            - if the node has no right child and is the left child of its parent,
                then the parent is the successor.
            - if the node is the right child of its parent, and itself has no right
                child, then the successor to this node is the successor of its parent,
                excluding this node.

        the first condition is the only one that matters for us when deleting a node
        from a binary search tree. However, the findSuccessor method has other uses
        that we will explore later.

    '''

    def findSuccessor(self):
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ


    '''
        the findMin method is called to find the minimum ket in a subtree,
        you should convince yourself that the minimum valued key in any
        bst is the leftmost child of the tree. therefore, the findMin method
        simply follows the leftChild references in each node of the subtree until
        it reaches a node that does not have a left child
    '''

    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current

    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    if self.isLeftChild():
                        self.parent.leftChild = self.rightChild
                    else:
                        self.parent.rightChild = self.rightChild
                    self.rightChild.parent = self.parent

## initialise the tree  -------------------------------------------------------
tree = BinarySearchTree()
MODULO = 1000000001
n = int(stdin.readline())
last_sum_result = 0
for i in range(n):
    line = stdin.readline().split()
    if line[0] == '+':
        ## add this mother to the tree  ---------------------------------------
        add_value = ((last_sum_result + int(line[1])) % MODULO)
        tree.put(key = add_value, val = add_value)
    elif line[0] == '-':
        ## delete this mother from the table  ---------------------------------
        delete_value = ((last_sum_result + int(line[1])) % MODULO)
        if delete_value in tree:
            tree.delete(key = delete_value)
    elif line[0] == '?':
        ## is this mother in the tree  ----------------------------------------
        find_value = ((last_sum_result + int(line[1])) % MODULO)
        find_value = find_value in tree
        if find_value:
            print("Found")
        else:
            print("Not found")
    else:
        l, r = int(line[1]), int(line[2])
        ## sum this range  ----------------------------------------------------
        last_sum_result = (tree.sum(low = ((last_sum_result + l) % MODULO)
                 , high = ((last_sum_result + r ) % MODULO)
                 )
              )
        print(last_sum_result)


