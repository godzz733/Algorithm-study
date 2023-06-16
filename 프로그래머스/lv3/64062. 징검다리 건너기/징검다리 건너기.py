def solution(stones, k):
    st = 1
    fi = 200000000
    ans = 0
    while (st<=fi):
        cnt = 0
        mid = (st+fi)//2
        for i in stones:
            if i-mid < 0:
                cnt += 1
                if cnt >= k:
                    break
            else:
                cnt = 0
            
        if cnt >= k:
            fi = mid -1
        else:
            st = mid +1
            ans = mid
    return ans