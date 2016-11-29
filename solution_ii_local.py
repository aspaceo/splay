## python3  -------------------------------------------------------------------

## we should be able to generate a submission that will fail on time  ---------


class Node:
    def __init__(self, key, left_child = None, right_child = None, parent = None, sum = 1):
        self.key, self.leftChild, self.rightChild, self.parent, self.sum = \
            key, left_child, right_child, parent, sum

    def __repr__(self):
        lc =  'No left child' if self.leftChild is None else self.leftChild.key
        rc = 'No right child' if self.rightChild is None else self.rightChild.key
        par = 'No parent' if self.parent is None else self.parent.key
        node_string = "Key: " + str(self.key) + \
            '\nLeft Child: ' + str(lc) + \
            '\nRight Child: ' + str(rc) + \
            '\nParent: ' + str(par) + \
            '\nSum: ' + str(self.sum)
        return node_string

    def hasLeftChild(self):
        return self.leftChild is not None

    def hasRightChild(self):
        return self.rightChild is not None

    def hasAnyChildren(self):
        return not self.isLeaf()

    def hasBothChildren(self):
        return self.hasLeftChild() and self.hasRightChild()

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def isRoot(self):
        return not self.parent

    def leftDescendant(self):
        if self.leftChild is None:
            return self
        else:
            return self.leftChild.leftDescendant()

    def rightAncestor(self):
        if self.parent is None:
            return None
        if self.key < self.parent.key:
            return self.parent
        else:
            return self.parent.rightAncestor()

    def next(self):
        if self.isLeaf() and self.isRoot():
            return None
        else:
            if self.rightChild is not None:
                return self.rightChild.leftDescendant()
            else:
                return self.rightAncestor()

    def replaceNodeData(self, key, left_child, right_child):
        self.key = key
        self.leftChild = left_child
        self.rightChild = right_child
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self
        ## we need to update the sum   ----------------------------------------



    def expire(self):
        if self.isLeaf():  ## node has no children  ---------------------------
            if self.parent and self.isRightChild():
                self.parent.rightChild = None
            elif self.parent and self.isLeftChild():
                self.parent.leftChild = None
        elif self.hasBothChildren():  ## node has at most one child  ----------
            successor = self.findSuccessor()
            successor.splicedOut()
            self.key = successor.key
            self.sum = successor.sum
        elif self.hasLeftChild():
            ## node has only left child  --------------------------------------
            if self.isLeftChild():
                self.leftChild.parent = self.parent
                self.parent.leftChild = self.leftChild
            else: ## node is a right child  -----------------------------------
                self.leftChild.parent = self.parent
                self.parent.rightChild = self.leftChild
        else:  ## node has only right child  ----------------------------------
            if self.isLeftChild():
                self.rightChild.parent = self.parent
                self.parent.leftChild = self.rightChild
            else:
                self.rightChild.parent = self.parent
                self.parent.rightChild = self.rightChild

    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current

    def findSuccessor(self):
        successor = None
        if self.hasRightChild():
            successor = self.rightChild.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    successor = self.parent
                else:
                    self.parent.rightChild = None
                    successor = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return successor


    def splicedOut(self):
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



    '''
        METHODS TO IMPLEMENT
        -----------------------

    '''


## create a splay tree  -------------------------------------------------------

class SplayTree:
    def __init__(self):
        self.root = None

    ## we initially define a bst tree insert  ---------------------------------
    def insert(self, node):
        ## if the root exists, call _insert
        if self.root:
            self._insert(self.root, node)
        else:
            self.root = node

    def _insert(self, current_node, node_to_insert):
        if node_to_insert.key < current_node.key:  ## insert on the left side -
            if current_node.hasLeftChild():
                self._insert(current_node.leftChild, node_to_insert)
            else:
                node_to_insert.parent = current_node
                current_node.leftChild = node_to_insert
        elif node_to_insert.key > current_node.key: ## insert on the right side
            if current_node.hasRightChild():
                self._insert(current_node.rightChild, node_to_insert)
            else:
                node_to_insert.parent = current_node
                current_node.rightChild = node_to_insert

    ## find a given key; if there, return 'Found', else 'Not found'
    def find(self, key):
        print(self._find_msg(key = key))


    def _find_msg(self, key):
        if self.root:
            return self._find(self.root, key)
        else:
            return 'Not found'

    def _find(self, current_node, key_to_find):
        if key_to_find > current_node.key:
            if current_node.hasRightChild():
                return self._find(current_node.rightChild, key_to_find)
            else:
                return 'Not found'
        elif key_to_find < current_node.key:
            if current_node.hasLeftChild():
                return self._find(current_node.leftChild, key_to_find)
            else:
                return 'Not found'
        elif key_to_find == current_node.key:
            return 'Found'

    def delete(self, key):
        if self.root:
            self._delete(self.root, key)
        else:
            pass

    def _delete(self, current_node, key_to_delete):
        ## three cases to consider; no children, node with one child, node with two children
        ## first find a match on the key
        if key_to_delete < current_node.key:
            if current_node.hasLeftChild():
                self._delete(current_node.leftChild, key_to_delete)
            else:
                pass
        elif key_to_delete > current_node.key:
            if current_node.hasRightChild():
                self._delete(current_node.rightChild, key_to_delete)
            else:
                pass
        elif key_to_delete == current_node.key:
            if current_node.isRoot():
                self.root = None
            else:
                current_node.expire()


    def _find_modi(self, key):
        if self.root:
            return self._find_modi_(self.root, key)
        else:
            return self.root

    def _find_modi_(self, current_node, key):
        if key == current_node.key:
            return current_node
        elif key > current_node.key:
            ## right side  ----------------------------------------------------
            if current_node.rightChild is None:
                return current_node
            else:
                return self._find_modi_(current_node.rightChild, key)
        elif key < current_node.key:
            ## left side  -----------------------------------------------------
            if current_node.leftChild is None:
                return current_node
            else:
                return self._find_modi_(current_node.leftChild, key)

    '''
        we think the problem with rangeSearch is the adding of nodes to a tree,
        causing fields to be overwritten.

        Instead, create a new node from the key of the original
    '''

    def rangeSearch(self, lower_bound, upper_bound):
        result_set = SplayTree()
        noode = self._find_modi(lower_bound)
        while noode and noode.key <= upper_bound:
            if noode.key >= lower_bound:
                 result_set.insert(Node(noode.key))
            noode = noode.next()
        return result_set

    def treeSum(self):
        if self.root is None:
            return 0
        return self._subTreeSum(self.root)

    def _subTreeSum(self, current_node):
        if current_node is None:
            return 0
        else:
            return current_node.key + self._subTreeSum(current_node.leftChild) + self._subTreeSum(current_node.rightChild)


from sys import stdin
from sys import setrecursionlimit
import os
os.chdir("/Users/p.whyte/Desktop/splay/tests")


## initialise the tree  -------------------------------------------------------
tree = SplayTree()
MODULO = 1000000001
## connect to file   ----------------------------------------------------------
input = open('83.txt', 'r')


setrecursionlimit(25000)

n = int(input.readline())
last_sum_result = 0
for i in range(n):
    line = input.readline().split()
    if line[0] == '+':
        ## add this mother to the tree  ---------------------------------------
        add_value = ((last_sum_result + int(line[1])) % MODULO)
        tree.insert(Node(add_value))
    elif line[0] == '-':
        ## delete this mother from the table  ---------------------------------
        delete_value = ((last_sum_result + int(line[1])) % MODULO)
        tree.delete(key = delete_value)
    elif line[0] == '?':
        ## is this mother in the tree  ----------------------------------------
        find_value = ((last_sum_result + int(line[1])) % MODULO)
        tree.find(find_value)
    else:
        l, r = int(line[1]), int(line[2])
        l, r = ((l + last_sum_result) % MODULO), ((r + last_sum_result) % MODULO)
        ## sum this range  ----------------------------------------------------
        last_sum_result = tree.rangeSearch(l, r).treeSum()
        print(last_sum_result)


