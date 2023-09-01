a = input()
ans = 0
for i in range(int(input())):
    tem = input()
    if a in tem*2:
        ans += 1
print(ans)