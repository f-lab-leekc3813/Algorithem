from collections import deque

def solution(n, m, section):
    answer = 0
    clear = []
    q = deque()
    now_len = section[0]
    for i in section:
        q.append(i)
    while q:
        cur = q.popleft()
        if cur > now_len + m -1:
            now_len = cur
            answer += 1
    
    return answer + 1