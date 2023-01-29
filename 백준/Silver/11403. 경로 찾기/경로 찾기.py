import sys
input = sys.stdin.readline
n = int(input().rstrip())
arr = []
for i in range(n): #맵 정보
    a = [*map(int, input().rstrip().split())]
    arr.append(a)
for k in range(n):
    for a in range(n):
        for b in range(n):            
            if arr[a][k] + arr[k][b] == 2: # a->b로 가는길이 잇는지 전부 체크
                arr[a][b] = 1 # 있다면 표시
for i in range(n):
    print(' '.join(map(str , arr[i])))
