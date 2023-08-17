ans = 0
point = 0
dic = {'A+':4.5,'A0':4.0,'B+':3.5,'B0':3.0,'C+':2.5,'C0':2.0,'D+':1.5,'D0':1.0,'F':0.0}
for _ in range(20):
    arr = [*map(str,input().split())]
    if arr[2] == 'P':continue
    ans += float(arr[1])*float(dic[arr[2]])
    point += float(arr[1])
print(round(ans/point,4))