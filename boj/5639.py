import sys

class Node(object):
    def __init__(self, key):
        self.key = key
        self.left = self.right = None


class BST(object):
    def __init__(self):
        self.root = None

    def Insert(self, key):
        self.root = self._InsertValue(self.root, key)
        
    def _InsertValue(self, node, key):
        if node == None:
            return Node(key)
        if key < node.key:
            node.left = self._InsertValue(node.left, key)

        elif key > node.key:
            node.right = self._InsertValue(node.right, key)

        return node

    def PostOrder(self):
        def _PostOrder(root):
            if root is None:
                pass
            else:
                _PostOrder(root.left)
                _PostOrder(root.right)
                print(root.key)
        _PostOrder(self.root)


bst = BST()

while 1:
    try:
        bst.Insert(int(sys.stdin.readline()))
    except:
        break

'''
#test case
import random
a = [_ for _ in range(100000)]
for i in range(10001):
    bst.Insert(random.sample(a,1)[0])
'''


bst.PostOrder()