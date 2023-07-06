n = int(input())
arr_min = list(map(int ,input().split()))
arr_max = arr_min[::]
for i in range(n-1):
    a,b,c = map(int,input().split())
    arr_min = [min(arr_min[0] + a, arr_min[1] + a),min(arr_min[1] + b, arr_min[0] + b,arr_min[2]+b),min(arr_min[2] + c, arr_min[1] + c)]
    arr_max = [max(arr_max[0] + a, arr_max[1] + a),max(arr_max[1] + b, arr_max[0] + b,arr_max[2]+b),max(arr_max[2] + c, arr_max[1] + c)]
print(max(arr_max),min(arr_min))