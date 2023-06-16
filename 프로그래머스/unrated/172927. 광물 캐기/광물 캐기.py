ans = 987654321
def solution(picks, minerals):
    pick = {0 : 0, 1 : 0, 2 : 0}
    for i in range(3):
        pick[i] = picks[i]
    print(pick)
    min = []
    for i in range(0,len(minerals), 5):
        cnt1 = 0
        cnt2 = 0
        cnt3 = 0
        for j in minerals[i:i+5]:
            if j == 'diamond':
                cnt1 += 1
                cnt2 += 5
                cnt3 += 25
            elif j == 'iron':
                cnt1 += 1
                cnt2 += 1
                cnt3 += 5
            else:
                cnt1 += 1
                cnt2 += 1
                cnt3 += 1
        min.append((cnt1,cnt2,cnt3))
    dfs(0,min,0,len(min),pick)
    answer = ans
    print(min)
    return answer
def dfs(anss, min, cnt, n, pick):
    global ans
    if anss > ans:
        return
    if cnt == n or (not pick[0] and not pick[1] and not pick[2]):
        if anss < ans:
            ans = anss
        return
    for i in range(3):
        if pick[i]:
            pick[i] -= 1
            dfs(anss + min[cnt][i], min, cnt+1, len(min), pick)
            pick[i] += 1
    