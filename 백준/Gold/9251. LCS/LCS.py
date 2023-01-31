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