from itertools import combinations
alphabet_list = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
                 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

alpha_to_bit = {alphabet_list[i]: 1 << i for i in range(21)}



for tc in range(1,int(input())+1):
    n,m = map(int , input().split())
    _set = set()
    arr = []
    for i in range(n):
        word = set(list(input().rstrip()))
        if len(word)> m: continue
        _set = _set.union(word)
        tem = 0
        for j in word:
            tem |= alpha_to_bit[j]
        arr.append(tem)
    lst = list(_set)
    if len(_set) <= m:
        print(f'#{tc} {len(arr)}')
        continue
    ans = 0
    bits = []
    for i in lst:
        bits.append(alpha_to_bit[i])
    for i in combinations(bits,m):
        tem = 0
        for j in i:
            tem |= j
        temp = 0
        for j in arr:
            if j & tem == j:
                temp += 1
        ans = max(ans,temp)
    print(f'#{tc} {ans}')