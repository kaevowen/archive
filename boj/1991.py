class Node(object):
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

def PreOrder(node):
    print(node.data, end='')
    if node.left != '.':
        PreOrder(tree[node.left])
    if node.right != '.':
        PreOrder(tree[node.right])

def InOrder(node):
    if node.left != '.':
        InOrder(tree[node.left])
    print(node.data, end='')
    if node.right != '.':
        InOrder(tree[node.right])

def PostOrder(node):
    if node.left != '.':
        PostOrder(tree[node.left])
    if node.right != '.':
        PostOrder(tree[node.right])
    print(node.data, end='')

n = int(input())
tree = {}
for i in range(n):
    data = input().split(' ')
    tree[data[0]] = Node(data=data[0], left=data[1], right=data[2])

PreOrder(tree['A'])
print()
InOrder(tree['A'])
print()
PostOrder(tree['A'])
