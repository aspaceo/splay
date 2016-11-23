import unittest
import splayTree

'''
    Node functions to test
    - isRoot
    - isLeaf
    - hasLeftChild
    - hasRightChild
    - hasAnyChildren
    - isLeftChild
    - isRightChild
'''

class NodeTest(unittest.TestCase):

    ## assert node with no parent is root -------------------------------------
    def test_root_true(self):
        self.assertTrue(splayTree.Node(key = 1).isRoot())
    ## assert node with parent is not root  -----------------------------------
    def test_root_false(self):
        self.assertFalse(splayTree.Node(key = 10, parent = splayTree.Node(key = 5)).isRoot())

    ## assert node with no children is leaf
    def test_leaf_true(self):
        self.assertTrue(splayTree.Node(key = 1).isLeaf())
    ## assert node with children is not a leaf  -------------------------------
    def test_leaf_false(self):
        self.assertFalse(splayTree.Node(key = 1, left_child = splayTree.Node(key = 2)).isLeaf())

    ## hasLeftChild  ----------------------------------------------------------
    def test_leftChild_true(self):
        self.assertTrue(splayTree.Node(key = 1, left_child = splayTree.Node(key = 2)).hasLeftChild())
    def test_leftChild_false(self):
        self.assertFalse(splayTree.Node(key = 1).hasLeftChild())

    ##  has right child  ------------------------------------------------------
    def test_rightChild_true(self):
        self.assertTrue(splayTree.Node(key=1, right_child=splayTree.Node(key=2)).hasRightChild())
    def test_rightChild_false(self):
        self.assertFalse(splayTree.Node(key=1).hasRightChild())

    ##  has any children  -----------------------------------------------------
    ##  with a right child  ---------------------------------------------------
    def test_anyChild_left(self):
        self.assertTrue(splayTree.Node(key = 1, left_child = splayTree.Node(key=2)).hasAnyChildren())
    def test_anyChild_right(self):
        self.assertTrue(splayTree.Node(key=1, right_child=splayTree.Node(key=2)).hasAnyChildren())
    def test_anyChild_false(self):
        self.assertFalse(splayTree.Node(key=1).hasAnyChildren())

    ## can't check is left / right child until we create the tree  ------------




if __name__ == '__main__':
    unittest.main()

##run this if running from the command line



'''
suite = unittest.TestLoader().loadTestsFromTestCase(myTest)
unittest.TextTestRunner(verbosity = 2).run(suite)
'''