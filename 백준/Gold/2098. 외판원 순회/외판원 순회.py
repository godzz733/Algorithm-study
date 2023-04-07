n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
visited = [[None] * (1<<n) for _ in range(n)]
arrive = (1<<n) -1
INF = float('inf')

def find_path(last,visit):
    if visit == arrive:
        return arr[last][0] or INF
    
    if visited[last][visit] is not None:
        return visited[last][visit]
     
    temp = INF
    for city in range(n):
        if visit & (1<<city) == 0 and arr[last][city]:
            temp = min(temp, find_path(city, visit | (1<<city)) + arr[last][city])
    visited[last][visit] = temp
    return temp

print(find_path(0,1<<0))