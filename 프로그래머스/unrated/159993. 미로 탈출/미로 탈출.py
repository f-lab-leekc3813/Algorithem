from collections import deque


def solution(maps):
    answer = -1
    row = len(maps)
    col = len(maps[0])
    lever = True
    # S의 위치 파악
    visited = [[False] * col for _ in range(row)]
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] == "S":
                start_row = i
                start_col = j
                break
    delta = [(1,0),(-1,0),(0,1),(0,-1)]
    
    queue = deque()
    queue.append((start_row,start_col,0))
    # 먼저 레버 당기기 E찾기
    le_row,le_col,le_len = 0 , 0 , 0
    while queue:
        cur_r,cur_c,cur_len = queue.popleft()
        # 레버 L을 찾았을때
        if maps[cur_r][cur_c] == "L":
            le_row,le_col,le_len = cur_r,cur_c, cur_len
            lever = False
            break
        for dr , dc in delta:
            next_r = cur_r + dr
            next_c = cur_c + dc
            if next_r >= 0 and next_r < row and next_c >= 0 and next_c < col:
                if maps[next_r][next_c] != "X" and not visited[next_r][next_c]:
                    queue.append((next_r, next_c, cur_len + 1))
                    visited[next_r][next_c] = True
    # 레버가 없을경우 바로 -1 리턴
    if lever:
        return -1
    #방문 초기화
    visited2 = [[False] * col for _ in range(row)]
    #레버 위치에서 다시 시작
    queue2 = deque()
    queue2.append((le_row,le_col,le_len))
    while queue2:
        cur_r,cur_c,cur_len = queue2.popleft()
        #종료지점
        if maps[cur_r][cur_c] == "E":
            answer = cur_len
            break
        for dr, dc in delta:
            next_r = cur_r + dr
            next_c = cur_c + dc
            if next_r >= 0 and next_r < row and next_c >= 0 and next_c < col:
                if maps[next_r][next_c] != "X" and not visited2[next_r][next_c]:
                    queue2.append((next_r, next_c, cur_len + 1))
                    visited2[next_r][next_c] = True  

    return answer