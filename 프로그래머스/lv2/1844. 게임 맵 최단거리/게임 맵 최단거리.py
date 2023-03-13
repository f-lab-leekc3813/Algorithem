from collections import deque

def solution(maps):
    answer = -1
    row = len(maps)
    col = len(maps[0])
    
    visited = [[False] * col for _ in range(row)]
    
    delta = [(1,0), (-1,0),(0,1),(0,-1)]
    
    queue = deque()
    queue.append((0,0,1))
    
    while queue:
        cur_r,cur_c,cur_len = queue.popleft()
        if cur_r == row - 1 and cur_c == col - 1:
            answer = cur_len
            break
        for dr, dc in delta:
            next_r = cur_r + dr
            next_c = cur_c + dc
            if next_r >= 0 and next_r < row and next_c >= 0 and next_c < col:
                if maps[next_r][next_c] == 1 and not visited[next_r][next_c]:
                    queue.append((next_r, next_c, cur_len + 1))
                    visited[next_r][next_c] = True
    return answer