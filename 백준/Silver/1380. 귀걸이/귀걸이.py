import sys;input = sys.stdin.readline
for k in range(1,10000):
    n = int(input())
    if not n: exit()
    a = list(input().rstrip() for _ in range(n))
    arr = set()
    for i in range((n<<1)-1):
        num,_ = map(str,input().split())
        if int(num) in arr: arr.remove(int(num))
        else: arr.add(int(num))
    print(k,a[arr.pop()-1])