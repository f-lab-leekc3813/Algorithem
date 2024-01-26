from itertools import combinations
from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int,input().split())) for _ in range(n)]

virus = []
answer = 1000000

# 바이러스의 좌표 찾기 및 보드 전처리
for r in range(n):
    for c in range(n):
        if board[r][c] == 0:
            board[r][c] = '_'
        elif board[r][c] == 1:
            board[r][c] = '-'
        elif board[r][c] == 2:
            virus.append([r,c])
            board[r][c] = '*'

# 유효한 범위 검사
def in_range(next_r, next_c):
    return 0 <= next_r < n and 0 <= next_c < n

def bfs(v):
    global answer
    queue = deque()
    for r,c in v:
        queue.append([r, c, 0])
    test_map = [board[i][:] for i in range(n)]

    max_level = 0
    while queue:
        r, c, level = queue.popleft()
        for dr, dc in [[-1,0],[1,0],[0,-1],[0,1]]:
            next_r, next_c, next_level = r+dr, c+dc, level+1
            if in_range(next_r, next_c):
								# 빈 칸일 때 max_level 갱신하며 진행
                if test_map[next_r][next_c] == '_':
                    test_map[next_r][next_c] = next_level
                    max_level = max(max_level, next_level)
                    queue.append([next_r, next_c, next_level])
								# 바이러스일 때 max_level 갱신 안함
                elif test_map[next_r][next_c] == '*':
                    test_map[next_r][next_c] = next_level
                    queue.append([next_r, next_c, next_level])
            
		# 모든 칸에 바이러스가 전파가 안된 경우
    for r in range(n):
        for c in range(n):
            if test_map[r][c] == '_':
                return
            
		# 정답 갱신
    answer = min(answer, max_level)
    return

# 활성화 시킬 바이러스 선정
for v in combinations(virus, m):
    for r,c in v:
        board[r][c] = 0
    bfs(v)
    for r,c in v:
        board[r][c] = '*'

# 모든 바이러스 조합을 검사한 후에도 정답이 갱신이 안 된 경우
if answer == 1000000:
    answer = -1
print(answer)
