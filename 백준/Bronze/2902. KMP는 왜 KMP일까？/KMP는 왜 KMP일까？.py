import string
arr = list(set(string.ascii_uppercase))
for i in input():
    if i in arr: print(i,end="")