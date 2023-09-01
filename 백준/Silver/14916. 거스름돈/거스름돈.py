n = int(input())
print(-1) if n==1 or n==3 else (print(n//5-1+(n%5+5)//2) if n%5&1 else print(n//5+n%5//2))