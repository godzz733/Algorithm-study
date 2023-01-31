import sys
input = sys.stdin.readline

a, b = map(str,input().rstrip().split())

arr = [['.' for i in range(len(a))] for _ in range(len(b))]
def same():
    for i in a:
        for j in b:
            if i==j:
                return a.index(i),b.index(j)

a_index, b_index = same()

for i in range(len(a)):
    arr[b_index][i] = a[i]

for i in range(len(b)):
    arr[i][a_index] = b[i]

for i in arr:
    print(''.join(i))