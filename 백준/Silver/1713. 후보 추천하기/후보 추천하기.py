import sys

input = sys.stdin.readline
n = int(input().rstrip())
m = int(input().rstrip())
arr = [*map(int, input().rstrip().split())]
test = []
for i in range(m):
    if len(test) == 0:
        test.append([arr[i], 1, 101])  # 번호, 추천수, 들어온 순서
    elif len(test)<n:
        cnt = 0
        for j in range(len(test)):
            if arr[i] == test[j][0]:
                test[j][1] += 1
                cnt += 1
        for j in range(len(test)):
            test[j][2] -= 1
        if cnt == 0:
            test.append([arr[i], 1, 101])
        cnt = 0
    elif len(test) == n:
        cnt = 0
        for j in range(len(test)):
            if arr[i] == test[j][0]:
                test[j][1] += 1
                cnt += 1
        for j in range(len(test)):
            test[j][2] -= 1
        if cnt == 0:
            test.sort(key=lambda x: (x[1], x[2]))
            del test[0]
            test.append([arr[i], 1, 101])
        cnt = 0
num = []
for i in test:
    num.append(i[0])
print(*sorted(num))