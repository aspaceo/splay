class bstNode():
    def __init__(self, key, parent = None, left = None, right = None, height = 0):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent
        self.height = height

    def __repr__(self):
        return "< bstNode, key:" + str(self.key) + " >"


class bst():
    def __init__(self, root = None):
        self.root = root

    def insert(self, key):
        ## you need to search the tree to find a place to put this node  ------
        ## you then need to create the node, instilling it with it's parent  --
        ## and adjust the parent's children  ------------------------------

        ## if the tree is empty  ----------------------------------------------
        if self.root == None:
            self.root = bstNode(key = key)
        ## if the tree is not empty, where should it go  ----------------------
        elif key < self.root.key:
            ## left sub tree  -------------------------------------------------
            if self.root.left == None:
                self.root.left = bstNode(key = key)
                self.root.height =+ 1
                self.root.left.parent = self.root
            ## if he doesn't have a child
            else:
                ## if he does have a child, recursive call
                bst(self.root.left).insert(key = key)
        elif key > self.root.key:
            ## right sub tree  ------------------------------------------------
            if self.root.right == None:
                self.root.right = bstNode(key = key)
                self.root.height =+ 1
                self.root.right.parent = self.root
            else:
                bst(self.root.right).insert(key = key)

    def __repr__(self):

