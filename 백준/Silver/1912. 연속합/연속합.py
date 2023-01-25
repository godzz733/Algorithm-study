import sys #한번도 안더하고 그냥 값 하나만 출력해도 됨
t = int(input())
arr = [*map(int,sys.stdin.readline().split())]
test = arr[::]
# arr_minus
for i in range(1,t): #앞에서부터 두개씩 더하면서 플러스가 뜨면 값이 커지니까 좋은거고 마이너스가 뜨면 안더하는게 좋으니까 0으로 처리함 (안더한다는 뜻)
    if arr[i-1] + arr[i] >0:
        arr[i] = arr[i-1] + arr[i]
    else: #두개 더한값이 마이너스면 그냥 0으로 만들어서 안더해버림
        arr[i] = 0
if sum(arr)==arr[0]: #어떠한 경우에도 더하는게 안좋다면
    print(max(test)) #원래 리스트에서 가장 큰 값을 출력
else: #더하는게 좋다면 더한 값중 가장 큰값을 출력
    print(max(arr))
