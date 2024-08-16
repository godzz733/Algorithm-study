import sys; input = sys.stdin.readline
idx = 1
num = 0
arr = []
ans = ["Party number 1"]
dic = {}
while 1:
    t = input().rstrip()
    if t == '#':
        if not num: 
            num += 1
            idx += 1
            tem = set()
            for i in arr:
                if i in tem: continue
                ansstr = f"{i} to "
                while i not in tem and i in dic:
                    tem.add(i)
                    ansstr += f"{dic[i]} to "
                    i = dic[i]
                ansstr = ansstr[:-4] + "."
                if ansstr != '.':
                    ans.append(ansstr)
            for i in ans:
                print(i)
            print()
            arr = []
            ans = [f"Party number {idx}"]
            dic = {}
            continue
        else: break
    num = 0
    a,b = map(str, t.split())
    arr.append(a)
    dic[a] = b