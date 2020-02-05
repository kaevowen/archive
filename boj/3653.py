from math import ceil, log

def init(A, tree, node, start, end):
    if start == end:
        tree[node] = A[node]
    else:
        mid = (start+end)//2
        tree[node] = init(node*2+1, start, 
            mid) + init(node*2+2, mid+1, end)

    return tree[node]

def summ(tree, node, start, end, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    return summ(tree, node*2, start, (start, end)//2,
     left, right) + summ(tree, node*2+1, 
     (start+end)//2+1, end, left, right)

A = [1,2,3,4,5,6,7,8,9,10]
N = 10
h = ceil(log(N, 2))
tree = [0 for i in range(1<<(h+1))]

#def init(A, tree, node, start, end):
init(A, tree, 0, 0, N-1)

summ(tree,1,2,3,4,5)