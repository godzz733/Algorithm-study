arr = [0,0,1]
for i in range(2,101):
    arr.append(arr[-1]+i)
n,m = map(int,input().split())
for i in range(m,101):
	if not ((n - arr[i]) % i) and (n - arr[i]) // i >= 0:
		for i in range(((n - arr[i]) // i),((n - arr[i]) // i) + i):
			print(i,end=' ')
		break
else:
	print(-1)