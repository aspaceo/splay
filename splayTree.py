
class Node:
    def __init__(self, key, left_child = None, right_child = None, parent = None, sum = 1):
        self.key, self.leftChild, self.rightChild, self.parent, self.sum = \
            key, left_child, right_child, parent, sum

    def __repr__(self):
        lc =  'No left child' if self.leftChild is None else self.leftChild.key
        rc = 'No right child' if self.rightChild is None else self.rightChild.key
        node_string = "Key: " + str(self.key) + \
            '\nLeft Child: ' + str(lc) + \
            '\nRight Child: ' + str(rc) + \
            '\nSum: ' + str(self.sum)
        return node_string

    def hasLeftChild(self):
        return self.leftChild is not None

    def hasRightChild(self):
        return self.rightChild is not None

    def hasAnyChildren(self):
        return not self.isLeaf()

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def isRoot(self):
        return not self.parent

    def replaceNodeData(self, key, left_child, right_child):
        self.key = key
        self.leftChild = left_child
        self.rightChild = right_child
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self
        ## we need to update the sum   ----------------------------------------


    '''
        METHODS TO IMPLEMENT
        -----------------------


        hasAnyChildren
        hasBothChildren
        replaceNodeData
        findSuccessor
        findMin
        spliceOut

    '''
