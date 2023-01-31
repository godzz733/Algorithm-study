import sys

input = sys.stdin.readline
word1 = list(str(input().rstrip()))
word2 = list(str(input().rstrip()))
arr = [[0 for _ in range(1+len(word2))] for _ in range(1+len(word1))]
for i in range(1,len(word1)+1):
    for k in range(1,len(word2)+1):
        if word2[k-1] != word1[i-1]:
            arr[i][k] = max(arr[i-1][k], arr[i][k-1])
        else:
            arr[i][k] = arr[i-1][k-1] + 1
print(arr[len(word1)][len(word2)])
result = []
def lcs(x,y):
    if arr[x][y] == 0:
        return False
    if arr[x][y] == arr[x-1][y] and arr[x][y]!=arr[x][y-1]:
        lcs(x-1,y)
    elif arr[x][y] == arr[x][y-1] and arr[x][y]!=arr[x-1][y]:
        lcs(x,y-1)
    elif arr[x][y] != arr[x][y-1] and arr[x][y] != arr[x-1][y]:
        result.append(word1[x-1])
        lcs(x-1,y-1)
    else:
        lcs(x-1,y)
lcs(len(word1),len(word2))
print(''.join(result[::-1]))

