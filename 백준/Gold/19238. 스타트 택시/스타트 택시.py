from collections import deque
import sys

input = sys.stdin.readline

# 백준 입력 형식, (1,1)부터 시작으로 설정되었기에 -1을 통해 (0,0)부터 시작하도록 전처리
n, m, fuel = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
tr, tc = map(int,input().split())
tr -= 1
tc -= 1
passenger = {}
for i in range(m):
    pr, pc, pdr, pdc = list(map(int, input().split()))
    passenger[(pr-1, pc-1)] = (pdr-1, pdc-1)

answer = 0

# 유효한 범위 검사
def in_range(next_r, next_c):
    return 0 <= next_r < n and 0 <= next_c < n

# 택시가 승객까지 가는 경우
def pickup(tr, tc):
    queue = deque([[tr, tc, 0]])
    visited = set([(tr, tc)])
    candidate = []
    min_distance = 1000000
    
    while queue:
        cur_r, cur_c, cur_d = queue.popleft()
				# 가장 짧은 거리에 위치한 승객과의 거리를 초과해 이동한 경우
        if cur_d > min_distance:
            break
				# 승객 위치에 도착한 경우 후보군에 추가
        if (cur_r, cur_c) in passenger:
            candidate.append((cur_r, cur_c))
            min_distance = cur_d
        for dr, dc in [[-1,0],[1,0],[0,-1],[0,1]]:
            next_r, next_c, next_d = cur_r+dr, cur_c+dc, cur_d+1
            if (next_r, next_c) in visited:
                continue
            if in_range(next_r, next_c) and board[next_r][next_c] != 1:
                queue.append([next_r, next_c, next_d])
                visited.add((next_r, next_c))
    
    return candidate, min_distance

# 승객을 태우고 목적지로 가는 경우
def go_dest(tr, tc):
    pdr, pdc = passenger[(tr, tc)]
    del passenger[(tr, tc)]
    queue = deque([[tr, tc, 0]])
    visited = set([(tr, tc)])
    
    while queue:
        cur_r, cur_c, cur_d = queue.popleft()
				# 목적지에 도착한 경우
        if cur_r == pdr and cur_c == pdc:
            return cur_r, cur_c, cur_d
        for dr, dc in [[-1,0],[1,0],[0,-1],[0,1]]:
            next_r, next_c, next_d = cur_r+dr, cur_c+dc, cur_d+1
            if (next_r, next_c) in visited:
                continue
            if in_range(next_r, next_c) and board[next_r][next_c] != 1:
                queue.append([next_r, next_c, next_d])
                visited.add((next_r, next_c))
		# 목적지에 도착할 수 없는 경우
    return pdr, pdc, 10000000

while fuel > 0 and len(passenger) != 0:
		# 가장 짧은 거리에 있는 승객들 찾기
    cand, used_fuel = pickup(tr, tc)
		# 연료가 부족한 경우 종료
    if used_fuel > fuel or len(cand) == 0:
        answer = -1
        break
		# 승객 선정
    tr, tc = sorted(cand)[0]
    fuel -= used_fuel
		# 목적지 까지 이동
    pdr, pdc, used_fuel = go_dest(tr, tc)
		# 연료가 부족한 경우 종료
    if used_fuel > fuel:
        answer = -1
        break
    fuel += used_fuel
    tr, tc = pdr, pdc
    
if answer == -1:
    print(-1)
else:
    print(fuel)