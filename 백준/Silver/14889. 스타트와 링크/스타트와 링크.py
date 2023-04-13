import copy

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
num_arr = [i for i in range(1, n + 1)]
result = []
food_result = []
for i in range(1 << n):
    li = []
    for j in range(n):
        if i & (1 << j):
            li.append(num_arr[j])
    result.append(li)
food_set = []

for i in result:
    if len(i) == n / 2:
        food_set.append(i)
for food in food_set:
    A_food = 0
    B_food = 0
    food_arr = []
    test = copy.deepcopy(num_arr)
    for j in food:
        test.remove(j)
    for i in food:
        for k in food:
            A_food += arr[i-1][k-1]
    for i in test:
        for k in test:
            B_food += arr[i - 1][k - 1]
    food_result.append(abs(A_food - B_food))
print(min(food_result))
