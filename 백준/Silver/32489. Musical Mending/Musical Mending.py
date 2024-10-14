import sys; input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))  

t = [arr[i] - i for i in range(n)]
t.sort()
diff = t[n//2]
print(sum(abs(t[i]-diff) for i in range(n)))