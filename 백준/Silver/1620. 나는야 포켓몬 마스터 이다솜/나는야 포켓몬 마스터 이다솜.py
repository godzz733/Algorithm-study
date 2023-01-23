import sys
a,b = map(int, input().split())
lis_arr = {}

result = []
for i in range(1,a+1):
    pokemon = str(sys.stdin.readline().rstrip())
    lis_arr[pokemon]=i
prob_dict = {v:k for k,v in lis_arr.items()}
for _ in range(b):
    prob = str(sys.stdin.readline().rstrip())
    try:
        if type(int(prob)) == int:
            print(prob_dict[int(prob)])
    except:
        print(lis_arr[prob])
