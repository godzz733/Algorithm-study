import sys;input = sys.stdin.readline
n = int(input())
arr = [input() for _ in range(n)]
if arr == sorted(arr):print('INCREASING')
elif arr == sorted(arr, reverse=True):print('DECREASING')
else:print('NEITHER')