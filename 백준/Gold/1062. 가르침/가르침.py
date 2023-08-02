from itertools import combinations
alphabet_list = ['b', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 's', 'u', 'v', 'w', 'x', 'y', 'z']

alpha_to_bit = {alphabet_list[i]: 1 << i for i in range(21)}

n,m = map(int ,input().split())
_set = set()
arr = []
for i in range(n):
    word = list(input().rstrip())
    _set = _set.union(set(word))
    tem = 0
    for j in set(word):
        if j != 'a' and j != 'n' and j != 't' and j != 'i' and j != 'c':
            tem |= alpha_to_bit[j]
    arr.append(tem)
_set = _set.difference(set(['a','n','t','i','c']))
lst = list(_set)
if len(_set) <= m-5:
    print(n)
elif m < 5:
    print(0)
else:
    m -= 5
    ans = 0
    for i in combinations(lst,m):
        tem = 0
        for j in i:
            tem |= alpha_to_bit[j]
        temp = 0
        for j in arr:
            if tem & j == j:
                temp += 1
        ans = max(ans,temp)
    print(ans)