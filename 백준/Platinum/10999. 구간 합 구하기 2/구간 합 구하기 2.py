import sys; input = sys.stdin.readline
import math
n,m,k = map(int,input().split())
arr = [int(input()) for _ in range(n)]
tree = [0] * (1 << (math.ceil(math.log2(n)) + 1))
laze = [0] * (1 << (math.ceil(math.log2(n)) + 1))
def init(node,s,e):
    if s == e:
        tree[node] = arr[s]
    else:
        init(node*2,s,(s+e)//2)
        init(node*2|1,((s+e)//2)+1,e)
        tree[node] = tree[node*2] + tree[node*2|1]

def update_lazy(node,s,e):
    if laze[node] != 0:
        tree[node] += (e-s+1)*laze[node]
        if s != e:
            laze[node*2] += laze[node]
            laze[node*2|1] += laze[node]
        laze[node] = 0

def update_range(node,s,e,l,r, diff):
    update_lazy(node,s,e)
    if l > e or r < s: return
    if l <= s and e <= r: 
        tree[node] += (e-s+1) * diff
        if (s != e):
            laze[node << 1] += diff
            laze[node << 1 | 1] += diff
        return
    update_range(node*2,s,(s+e)//2,l,r,diff)
    update_range(node*2 | 1,((s+e)//2) + 1,e,l,r,diff)
    tree[node] = tree[node*2] + tree[node*2|1]    

def query(node,s,e,l,r):
    update_lazy(node,s,e)
    if l > e or r < s: return 0
    if l <= s and e <= r: return tree[node]
    lsum = query(node*2,s,(s+e)//2,l,r)
    rsum = query(node*2 | 1,((s+e)//2) + 1,e,l,r)
    return lsum + rsum

init(1,0,n-1)

for i in range(m+k):
    lst = list(map(int,input().split()))
    if lst[0] == 1:
        update_range(1,0,n-1,lst[1]-1,lst[2]-1,lst[3])
    else:
        print(query(1,0,n-1,lst[1]-1,lst[2]-1))