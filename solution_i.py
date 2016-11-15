import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

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


def main():
    my_tree = binaryTree()
    n = int(sys.stdin.readline())
    for i in range(n):
        this_tuple = tuple(sys.stdin.readline().split())
        my_tree.add(this_tuple)
    my_tree.inOrderTrav(0); print('')
    my_tree.preOrderTrav(0); print('')
    my_tree.postOrderTrav(0); print('')

threading.Thread(target=main).start()