import sys

class node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
class tree:
    def __init__(self):
        self.root = None
    def insert(self,data):
        if(self.root == None):
            self.root = node(data)
        else:
            self._insert(self.root,data)
    def _insert(self,cur_node,data):
        if(data < cur_node.value):
            if(cur_node.left == None):
                cur_node.left = node(data)
            else:
                self._insert(cur_node.left,data)
        else:
            if(cur_node.right == None):
                cur_node.right = node(data)
            else:
                self._insert(cur_node.right,data)
    def postorder(self):
        if(self.root != None):
            self._postorder(self.root)
    def _postorder(self,cur_node):
        if(cur_node!=None):
            self._postorder(cur_node.left)
            self._postorder(cur_node.right)
            print(cur_node.value)


BST = tree()            

while 1:
    try:
        BST.Insert(int(sys.stdin.readline()))
    except:
        break