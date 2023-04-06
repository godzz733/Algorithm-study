def a_sum(cnt,num):
    if cnt == n//2:
        a.append(num)
        return
    a_sum(cnt+1,num+arr[cnt])
    a_sum(cnt+1,num)
def b_sum(cnt,num):
    if cnt == n:
        b.append(num)
        return
    b_sum(cnt+1,num+arr[cnt])
    b_sum(cnt+1,num)

n,m = map(int,input().split())
arr = list(map(int,input().split()))
a = []
b = []
a_sum(0,0)
b_sum(n//2,0)
a.sort()
b.sort()
result = 0
i = 0
j = len(b)-1
while i<len(a) and j>=0:
    if a[i] + b[j] == m:
        tema = a[i]
        temb = b[j]
        cnta = 0
        cntb = 0
        while i<len(a) and a[i] == tema:
            i += 1
            cnta += 1
        while j>=0 and b[j] == temb:
            j -= 1
            cntb += 1
        result += cnta * cntb
    elif a[i] + b[j] > m:
        j -= 1
    else:
        i += 1
if m == 0:
    result -=1
print(result)

