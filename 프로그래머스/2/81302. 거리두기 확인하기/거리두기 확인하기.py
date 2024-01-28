from collections import deque

def solution(places):
    answer = []
    
    def in_range(row,col):
        return 0 <= row < 5 and 0 <= col < 5
    
    def bfs(cur_place, start_r, start_c):
        
        visited = [[False] * 5 for _ in range(5)]
        start = (start_r, start_c,0)
        queue = deque()
        queue.append(start)
        while queue:
            cur_r, cur_c, cur_level = queue.popleft()
            visited[cur_r][cur_c] = True
            if cur_level != 0:
                if cur_place[cur_r][cur_c] == 'P':
                    return False

            for dr, dc in [[1,0],[-1,0],[0,1],[0,-1]]:
                next_r, next_c = cur_r + dr, cur_c + dc
                if in_range(next_r, next_c):
                    if cur_place[next_r][next_c] != 'X' and not visited[next_r][next_c]:
                        next_level = cur_level + 1
                        if next_level <= 2:
                            queue.append((next_r,next_c,next_level))
                    
        return True

    
    for i in range(len(places)):
        cur_place = places[i]
        tmp = 0
        for j in range(len(cur_place)):
            for k in range(len(cur_place[0])):
                if cur_place[j][k] == "P":
                    now_result = bfs(cur_place,j,k)
                    if not now_result:
                        tmp += 1
        if tmp != 0:
            answer.append(0)
        else:
            answer.append(1)
                          
    return answer