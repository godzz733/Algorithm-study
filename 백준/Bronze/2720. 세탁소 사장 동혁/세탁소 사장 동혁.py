arr = [25,10,5,1]
for _ in range(int(input())):
    n = int(input())
    ans = []
    for i in arr:
        ans.append(n//i)
        n%= i
    print(*ans)