import math
def init(arr, tree, node, start, end):
    if start == end:
        tree[node] = arr[start]
    else:
        init(arr,tree,node*2, start, (start+end)//2)
        init(arr,tree,node*2+1,(start+end)//2+1,end)
        tree[node] = tree[node*2] + tree[node*2+1]

def update(arr, tree, node, start, end, index, val):
    if index < start or index > end:
        return
    if start == end:
        arr[index] = val
        tree[node] = val
        return
    update(arr, tree, node*2, start, (start+end)//2, index, val)
    update(arr, tree, node*2+1, (start+end)//2+1, end, index, val)
    tree[node] = tree[node*2] + tree[node*2+1]

def query(tree,node,start,end,left,right):
    if left>end or right<start:
        return 0
    if left<=start and end<=right:
        return tree[node]
    lsum = query(tree,node*2,start,(start+end)//2,left,right)
    rsum = query(tree,node*2+1,(start+end)//2+1,end,left,right)
    return lsum + rsum


n, m, k  = map(int, input().split())
arr = [int(input()) for _ in range(n)]
h = math.ceil(math.log2(n))
size = 1<<(h+1)
tree = [0] * size
m += k
init(arr,tree,1,0,n-1)
for _ in range(m):
    command, t1, t2 = map(int,input().split())
    if command == 1:
        index, val = t1, t2
        update(arr,tree,1,0,n-1,index-1,val)
    else:
        left, right = t1, t2
        print(query(tree,1,0,n-1,left-1,right-1))