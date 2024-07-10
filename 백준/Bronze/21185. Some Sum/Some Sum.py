import sys;input = sys.stdin.readline().rstrip

n = int(input())
if n & 1: print("Either")
elif n & 2: print("Odd")
else: print("Even")