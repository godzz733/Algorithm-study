n,m = map(int, input().split())
arr = [i for i in range(n+1)]
for _ in range(m):
    a, b = map(int,input().split())
    if b-a == 1:arr[a],arr[b] = arr[b],arr[a]
    elif a==b: pass
    elif (b-a)%2 == 0:
        for i in range((b-a)//2):
            arr[a+i],arr[b-i] = arr[b-i],arr[a+i]
    else:
        for i in range((b-a)//2+1):
            arr[a+i],arr[b-i] = arr[b-i],arr[a+i]
print(*arr[1:])