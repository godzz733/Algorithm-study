import math

def init(arr,tree,node,start,end): # 트리 만들기
    if start == end: # 만약 리프노드라면
        tree[node] = arr[start] # 그 자리가 배열의 값
    else:
        init(arr,tree,node*2,start,(start+end)//2) #왼쪽
        init(arr,tree,node*2+1,(start+end)//2+1,end) #오른쪽
        tree[node] = tree[node*2] + tree[node*2+1]

def update(arr,tree,node,start,end,index,val): # 값 업데이트
    if start>index or end<index: #만약 인덱스가 범위를 넘어갓다면 그냥 리턴
        return
    if start == end: # 만약 변경되는 인덱스인 리프노드에 도달햇다면 값을 변경
        arr[index] = val
        tree[node] = val
        return
    update(arr,tree,node*2,start,(start+end)//2,index,val)
    update(arr,tree,node*2+1,(start+end)//2+1,end,index,val)
    tree[node] = tree[node*2] + tree[node*2+1] # 리프노드가 변경 되엇으니 그 부모들의 값도 변경됨


def query(tree,node,start,end,left,right):
    if right<start or left>end:
        return 0
    if left<=start and right>=end:
        return tree[node]
    lsum = query(tree,node*2,start,(start+end)//2,left,right)
    rsum = query(tree,node*2+1,(start+end)//2+1,end,left,right)
    return lsum + rsum
n, m, k = map(int,input().split())
arr = [int(input()) for _ in range(n)]
h = math.ceil(math.log2(n)) # 트리의 높이
size = 1 << (h+1) # 트리의 크기 (2**h+1 -1)
tree = [0] * size
init(arr,tree,1,0,n-1)
m += k # 총 연산 수는 m + k
for _ in range(m):
    a, b, c = map(int,input().split()) # 무슨 연산인지, b,c
    if a == 1:
        update(arr,tree,1,0,n-1,b-1,c)
    else:
        print(query(tree,1,0,n-1,b-1,c-1))
