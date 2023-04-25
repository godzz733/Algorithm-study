import sys, math
input = sys.stdin.readline
def init_max(node,start,end):
    if start == end:
        tree_max[node] = arr[start]
    else:
        mid = (start+end)//2
        init_max(node*2,start,mid)
        init_max(node*2+1,mid+1,end)
        tree_max[node] = max(tree_max[node*2],tree_max[node*2+1])

def init_min(node,start,end):
    if start == end:
        tree_min[node] = arr[start]
    else:
        mid = (start+end)//2
        init_min(node*2,start,mid)
        init_min(node*2+1,mid+1,end)
        tree_min[node] = min(tree_min[node*2],tree_min[node*2+1])

def query_max(node,start,end,left,right):
    if right<start or left>end:
        return 0
    if left<=start and right>=end:
        return tree_max[node]
    mid = (start+end)//2
    l = query_max(node*2,start,mid,left,right)
    r = query_max(node*2+1,mid+1,end,left,right)
    return max(l,r)
def query_min(node,start,end,left,right):
    if right<start or left>end:
        return 1000000001
    if left<=start and right>=end:
        return tree_min[node]
    mid = (start+end)//2
    l = query_min(node*2,start,mid,left,right)
    r = query_min(node*2+1,mid+1,end,left,right)
    return min(l,r)

n, m = map(int,input().split())
arr = [int(input()) for _ in range(n)]
h = math.ceil(math.log2(n))
size = 1 << (h+1)
tree_max = [0] * size
tree_min = [1000000001] * size
init_max(1,0,n-1)
init_min(1,0,n-1)
for _ in range(m):
    a, b = map(int,input().split())
    print(query_min(1,0,n-1,a-1,b-1), query_max(1,0,n-1,a-1,b-1))

