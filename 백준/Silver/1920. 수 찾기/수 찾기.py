n = int(input())
lst = set()
a = [*map(str,input().split())]
for i in a:
    lst.add(i)
m = int(input())
b = [*map(str,input().split())]
for i in b:
    if i in lst:
        print(1)
    else:
        print(0)