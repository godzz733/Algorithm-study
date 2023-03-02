square = set()
n = int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i*j <= n and (j,i) not in square:
            square.add((i,j))
print(len(square))
