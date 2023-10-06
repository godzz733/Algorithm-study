def solution(dirs):
    answer = 0
    dic = {'L' : (-1,0), 'R' : (1,0), 'D' : (0,-1), 'U' : (0,1)}
    _set = set()
    x = y = 0
    for i in dirs:
        dx, dy = dic[i]
        nx = x + dx
        ny = y + dy
        if nx < -5 or nx > 5 or ny < -5 or ny > 5: continue
        jo = ''.join([str(x),',',str(y),',',str(nx),',',str(ny)])
        re = ''.join([str(nx),',',str(ny),',',str(x),',',str(y)])
        if jo not in _set and re not in _set:
            answer += 1
            _set.add(jo)
            _set.add(re)
        x,y = nx, ny
    return answer