import bisect, math,sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
size = math.ceil(math.log2(n))+1

tree = [[] for _ in range(1<<size)]

def merge(left,right):
    tem = []
    i = j = 0
    l = len(left)
    r = len(right)
    while 1:
        if i == l:
            for k in range(j,r):
                tem.append(right[k])
            break
        if j == r:
            for k in range(i,l):
                tem.append(left[k])
            break
        if left[i] < right[j]:
            tem.append(left[i])
            i += 1
        else:
            tem.append(right[j])
            j += 1
    return tem
def init(node,start,end):
    if start == end:
        tree[node].append(arr[start-1])
        return
    mid = start + end >> 1
    init(node<<1, start, mid)
    init(node<<1|1, mid+1, end)
    tree[node] = merge(tree[node<<1],tree[node<<1|1])

def query(node,s,e,l,r,k):
    if e<l or s>r: return 0
    if s >= l and e <= r:
        return len(tree[node]) - bisect.bisect_right(tree[node],k)
    mid = s + e >> 1
    return query(node<<1,s,mid,l,r,k) + query(node<<1|1,mid+1,e,l,r,k)
    

init(1,0,n)

for _ in range(int(input())):
    a,b,c = map(int,input().split())
    print(query(1,0,n,a,b,c))