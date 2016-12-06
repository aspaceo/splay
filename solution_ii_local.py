##  imports  ------------------------------------------------------------------
from sys import stdin
from sys import setrecursionlimit
import os
##setrecursionlimit(25000)

## load splayTree  ------------------------------------------------------------
os.chdir("/Users/Paul/Documents/Coursera/SPEC_Data Structures and Algorithms/ii_Data Structures/assignments/week 5 - search trees/scratchpad")
import splayTree

## the instruction file  ------------------------------------------------------
os.chdir("/Users/Paul/Documents/Coursera/SPEC_Data Structures and Algorithms/ii_Data Structures/assignments/week 5 - search trees/Starters PA4/set_range_sum/tests")
input = open('36.txt', 'r')

## initialise the tree  -------------------------------------------------------
tree = SplayTree()
MODULO = 1000000001



n = int(input.readline())
n_master = 137

last_sum_result = 0
for i in range(n_master):
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


