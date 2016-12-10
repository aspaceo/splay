import unittest
import splayTree
import sys
from io import StringIO

'''
    tests to implement  ---


    next
    replaceNodeData
    findMin
    findSuccessor
    splicedOut
    leftDescendant
    rightAncestor

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

    ## test left descendant  --------------------------------------------------
    def test_leftDescendant_none(self):
        a = splayTree.Node(key = 20)
        self.assertEqual(a.leftDescendant().key, 20)

    # def test_rightAncestor_none(self):
    #     a = splayTree.Node(key = 20)
    #     self.assertEqual(a.rightAncestor().key)

    def test_leftDescendant(self):
        a = splayTree.Node(key = 20)
        b = splayTree.Node(key = 15)
        c = splayTree.Node(key = 17)
        d = splayTree.Node(key = 12)
        e = splayTree.Node(key = 14)
        f = splayTree.Node(key = 9)
        ## arrange nodes  -----------------------------------------------------
        f.parent, e.parent = d, d
        d.leftChild, d.rightChild = f, e

        d.parent, c.parent = b, b

        b.leftChild, b.rightChild = d, c

        b.parent = a

        a.leftChild = b

        self.assertEqual(a.leftDescendant().key, 9)

    ## test leftAncestor  -----------------------------------------------------
    def test_rightAncestor(self):
        a = splayTree.Node(key = 20)
        b = splayTree.Node(key = 15)
        c = splayTree.Node(key = 17)
        d = splayTree.Node(key = 12)
        e = splayTree.Node(key = 14)
        f = splayTree.Node(key = 9)
        ## arrange nodes  -----------------------------------------------------
        f.parent, e.parent = d, d
        d.leftChild, d.rightChild = f, e

        d.parent, c.parent = b, b

        b.leftChild, b.rightChild = d, c

        b.parent = a

        a.leftChild = b

        self.assertEqual(e.rightAncestor().key, 15)

    def test_next(self):
        a = splayTree.Node(key=20)
        b = splayTree.Node(key=15)
        c = splayTree.Node(key=17)
        d = splayTree.Node(key=12)
        e = splayTree.Node(key=14)
        f = splayTree.Node(key=9)
        ## arrange nodes  -----------------------------------------------------
        f.parent, e.parent = d, d
        d.leftChild, d.rightChild = f, e

        d.parent, c.parent = b, b

        b.leftChild, b.rightChild = d, c

        b.parent = a

        a.leftChild = b

        self.assertEqual(d.next().key, 14)

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

    def test_delete_big(self):
        inserts = [1000, 500, 1500, 250, 750, 625, 825, 626]
        my_tree = splayTree.SplayTree()
        for x in inserts:
            my_tree.insert(splayTree.Node(x))
        my_tree.delete(500)
        parent = my_tree.root.leftChild.rightChild.leftChild.parent.key
        self.assertEqual(parent, 750)

    ## test modified find   ---------------------------------------------------
    def test_find_modi_root(self):
        x = splayTree.SplayTree()
        l = [87, 35, 81, 23, 13, 84, 41, 5, 31, 30]
        for e in l:
            x.insert(splayTree.Node(e))
        self.assertEqual(x._find_modi(key = 87).key, 87)

    def test_find_modi_leaf(self):
        x = splayTree.SplayTree()
        l = [87, 35, 81, 23, 13, 84, 41, 5, 31, 30]
        for e in l:
            x.insert(splayTree.Node(e))
        self.assertEqual(x._find_modi(key = 41).key, 41)

    def test_find_modi_missing(self):
        x = splayTree.SplayTree()
        l = [87, 35, 81, 23, 13, 84, 41, 5, 31, 30]
        for e in l:
            x.insert(splayTree.Node(e))
        self.assertEqual(x._find_modi(key = 85).key, 84)

    def test_find_modi_empty_tree(self):
        x = splayTree.SplayTree()
        self.assertFalse(x._find_modi(10))


    def test_treeSum(self):
        x = splayTree.SplayTree()
        l = [87, 35, 81, 23, 13, 84, 41, 5, 31, 30]
        for e in l:
            x.insert(splayTree.Node(e))
        self.assertEqual(x.treeSum(), 430)

    def test_treeSum_empty(self):
        x = splayTree.SplayTree()
        self.assertEqual(x.treeSum(), 0)

    def testRangeSum_a(self):
        x = splayTree.SplayTree()
        l = [87, 35, 81, 23, 13, 84, 41, 5, 31, 30]
        for e in l:
            x.insert(splayTree.Node(e))
        self.assertEqual(x.rangeSearch(10, 30).treeSum(), 66)



'''
    tests required for ...

    _find_modi_

'''
















if __name__ == '__main__':
    unittest.main()

##run this if running from the command line



'''
suite = unittest.TestLoader().loadTestsFromTestCase(myTest)
unittest.TextTestRunner(verbosity = 2).run(suite)
'''