n = int(input())
arr = []
for _ in range(n):
    a,b = map(int,input().split())
    arr.append((a,b))
arr.sort()
st = fi = 0
st = arr[0][0]
fi = arr[0][1]
ans = 0
for i in range(1,n-1):
    a,b = arr[i][0],arr[i][1]
    if st<=a and fi>=b: continue
    elif fi<=a:
        ans += fi-st
        st,fi = a,b
    elif st<=a and b>=fi:
        fi = b
a,b= arr[n-1][0],arr[n-1][1]
if st<=a and fi>=b:
    ans += fi-st
elif fi<=a:
    ans += b-a + fi-st
elif st<=a and b>=fi:
    fi = b
    ans += fi-st
print(ans)