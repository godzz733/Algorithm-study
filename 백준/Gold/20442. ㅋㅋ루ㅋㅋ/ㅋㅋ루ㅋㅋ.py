arr = [*input()]
ans = arr.count('R')
st,fi = 0, len(arr)-1
lst = {'R' : ans, 'K' : len(arr)-ans}
if ans == len(arr) or lst['R'] == 0: pass
else:
    while st < len(arr) and arr[st] != 'K':
        lst['R'] -= 1
        st += 1
    while fi >= 0 and arr[fi] != 'K':
        lst['R'] -= 1
        fi -= 1
    ans = max(ans,lst['R'] + 2)
    cnt = 0
    while st < len(arr) and fi >=0 and st < fi:
        cnt += 1
        while st < len(arr) and arr[st] != 'K':
            lst['R'] -= 1
            st += 1
        while fi >= 0 and arr[fi] != 'K':
            lst['R'] -= 1
            fi -= 1
        if not st < len(arr) or not  fi >=0 or not st < fi or lst['R'] <= 0: break
        ans = max(ans,lst['R'] + cnt * 2)
        st += 1
        fi -= 1
print(ans)