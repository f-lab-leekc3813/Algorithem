from itertools import combinations
from collections import deque, Counter
import sys

input = sys.stdin.readline

# 백준 입력 형식
n, m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]

virus, empty = [], []
answer = 0

# 빈칸, 바이러스 위치 저장
for r in range(n):
    for c in range(m):
        if board[r][c] == 0:
            empty.append([r,c])
        elif board[r][c] == 2:
            virus.append([r,c])
            
# 유효한 범위 검사
def in_range(next_r, next_c):
    return 0 <= next_r < n and 0 <= next_c < m

# BFS로 구현했지만, DFS로 구현해도 된다. 
# DFS(재귀)로 구현해보면 조금 복잡해지는게 생긴다.
# 예를들어 tmp = [board[i][:] for i in range(n)] 이렇게 복사하는 코드 구현이 까다로워질 수 있고
# 또, BFS는 queue = deque(virus)를 이용해서 여러 바이러스를 동시에 확산시킬 수 있는데, DFS로 구현하면 DFS를 여러번 호출해야되서 번거로워진다.
def bfs():
    global answer
    tmp = [board[i][:] for i in range(n)]
    queue = deque(virus)
		
		# bfs를 통해 바이러스 전파
    while queue:
        r,c = queue.popleft()
        for dr, dc in [[-1,0],[1,0],[0,-1],[0,1]]:
            next_r, next_c = r+dr, c+dc
            if in_range(next_r, next_c):
                if tmp[next_r][next_c] == 0:
                    tmp[next_r][next_c] =2
                    queue.append((next_r,next_c))

		# 전파 완료 후 0, 1, 2 개수 세기
    count = Counter([])
    for row in tmp:
        count += Counter(row)

		# 빈칸 개수를 통해 정답 갱신
    answer = max(answer, count[0])
    return


# 새로운 벽 3개를 설치하는 경우의 수 (empty에 빈 칸을 저장한 이유)
for new_wall in combinations(empty, 3):
    row, col = [], []
    for r, c in new_wall:
        row.append(r)
        col.append(c)
        if board[r][c] != 0:
            break
    else:
        for i in range(3):
            board[row[i]][col[i]] = 1
        bfs()
        for i in range(3):
            board[row[i]][col[i]] = 0

print(answer)