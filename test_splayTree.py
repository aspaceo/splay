import unittest
import splayTree
import sys
from io import StringIO

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

    ## has both children  -----------------------------------------------------
    def test_bothChildren_true(self):
        self.assertTrue(splayTree.Node(key = 1, left_child = splayTree.Node(key=2), right_child = splayTree.Node(key=3)).hasBothChildren())
    def test_bothChildren_falseLeft(self):
        self.assertFalse(splayTree.Node(key=1, left_child=splayTree.Node(key=2)).hasBothChildren())
    def test_bothChildren_falseRight(self):
        self.assertFalse(splayTree.Node(key=1, right_child=splayTree.Node(key=2)).hasBothChildren())
    def test_bothChildren_false(self):
        self.assertFalse(splayTree.Node(key=1).hasBothChildren())

    def test_isLeftChild_true(self):
        x = splayTree.SplayTree()
        x.insert(splayTree.Node(key=2))
        x.insert(splayTree.Node(key=1))
        self.assertTrue(x.root.leftChild.isLeftChild())

    def test_isRightChild_true(self):
        x = splayTree.SplayTree()
        x.insert(splayTree.Node(key=1))
        x.insert(splayTree.Node(key=2))
        self.assertTrue(x.root.rightChild.isRightChild())



class splayTest(unittest.TestCase):

    ##  -----------------------------------------------------------------------
    ## test insert  -----------------------------------------------------------

    def test_insert(self):
        x = splayTree.SplayTree()
        x.insert(splayTree.Node(key = 1))
        self.assertFalse(x.root is None)

    def test_insert_key(self):
        x = splayTree.SplayTree()
        x.insert(splayTree.Node(key = 1))
        self.assertEqual(x.root.key, 1)

    def test_insert_node_right(self):
        ## assert node is inserted to right child of root  --------------------
        x = splayTree.SplayTree()
        x.insert(splayTree.Node(key=1))
        x.insert(splayTree.Node(key=2))
        self.assertEqual(x.root.rightChild.key, 2)

    def test_insert_node_left(self):
        ## assert node is inserted to left child of root  ---------------------
        x = splayTree.SplayTree()
        x.insert(splayTree.Node(key=2))
        x.insert(splayTree.Node(key=1))
        self.assertEqual(x.root.leftChild.key, 1)

    def test_insert_node_left_left(self):
        x = splayTree.SplayTree()
        x.insert(splayTree.Node(key=3))
        x.insert(splayTree.Node(key=2))
        x.insert(splayTree.Node(key=1))
        self.assertEqual(x.root.leftChild.leftChild.key, 1)

    ##  -----------------------------------------------------------------------
    ## test find method  ------------------------------------------------------
    def test_find_empty(self):
        x = splayTree.SplayTree()
        self.assertEqual(x._find_msg(1), 'Not found')
    def test_find_root(self):
        x = splayTree.SplayTree()
        x.insert(splayTree.Node(1))
        self.assertEqual(x._find_msg(1), 'Found')
    def test_find_removed(self):
        x = splayTree.SplayTree()
        x.insert(splayTree.Node(1))
        x.delete(key = 1)
        self.assertEqual(x._find_msg(1), 'Not found')

    def test_find_removed_big_not_found(self):
        x = splayTree.SplayTree()
        x.insert(splayTree.Node(10))
        x.insert(splayTree.Node(20))
        x.insert(splayTree.Node(2))
        x.insert(splayTree.Node(15))
        x.insert(splayTree.Node(8))
        x.insert(splayTree.Node(3))
        x.insert(splayTree.Node(1))
        x.insert(splayTree.Node(18))
        x.insert(splayTree.Node(5))
        x.insert(splayTree.Node(13))
        x.insert(splayTree.Node(19))
        x.delete(10)
        self.assertEqual(x._find_msg(10), 'Not found')

    def test_find_removed_big_found(self):
        x = splayTree.SplayTree()
        x.insert(splayTree.Node(10))
        x.insert(splayTree.Node(20))
        x.insert(splayTree.Node(2))
        x.insert(splayTree.Node(15))
        x.insert(splayTree.Node(8))
        x.insert(splayTree.Node(3))
        x.insert(splayTree.Node(1))
        x.insert(splayTree.Node(18))
        x.insert(splayTree.Node(5))
        x.insert(splayTree.Node(13))
        x.insert(splayTree.Node(19))
        x.delete(15)
        self.assertEqual(x._find_msg(20), 'Found')

















if __name__ == '__main__':
    unittest.main()

##run this if running from the command line



'''
suite = unittest.TestLoader().loadTestsFromTestCase(myTest)
unittest.TextTestRunner(verbosity = 2).run(suite)
'''