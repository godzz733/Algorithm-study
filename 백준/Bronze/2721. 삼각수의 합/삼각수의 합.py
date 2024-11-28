import sys; input = sys.stdin.readline
lst = [0]+[i*(i+1)//2 for i in range(1,302)]
arr = [0]
for i in range(1,301):
    arr.append(arr[-1]+i*lst[i+1])

for _ in range(int(input())):
    n = int(input())
    print(arr[n])