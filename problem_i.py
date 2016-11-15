## implement a binary tree  ---------------------------------------------------

class binaryTree():
    def __init__(self):
        ## a list of tuples; (key, left, right)  ------------------------------
        self.tree = []
    ## add a node to the three  -----------------------------------------------
    def add(self, node_tuple):
        self.tree.append(node_tuple)
    ## in order traversal  ----------------------------------------------------
    def inOrderTrav(self, node):
        if node != -1:
            self.inOrderTrav(self.tree[node][1])
            print(self.tree[node][0], end = ' ', flush = True)
            self.inOrderTrav(self.tree[node][2])

    ## pre order traversal  ---------------------------------------------------
    def preOrderTrav(self, node):
        if node != -1:
            print(self.tree[node][0], end=' ', flush=True)
            self.preOrderTrav(self.tree[node][1])
            self.preOrderTrav(self.tree[node][2])

    ## post order traversal  --------------------------------------------------
    def postOrderTrav(self, node):
        if node != -1:
            self.postOrderTrav(self.tree[node][1])
            self.postOrderTrav(self.tree[node][2])
            print(self.tree[node][0], end=' ', flush=True)

my_tree = binaryTree()
a, b, c, d, e = (4, 1, 2), (2, 3, 4), (5, -1, -1), (1, -1, -1), (3, -1, -1)
my_tree.add(a)
my_tree.add(b)
my_tree.add(c)
my_tree.add(d)
my_tree.add(e)
my_tree.inOrderTrav(0); print('')
my_tree.preOrderTrav(0); print('')
my_tree.postOrderTrav(0); print('')
