from collections import defaultdict
from heapq import heappush, heappop

def solution(n, paths, gates, summits):
    summits.sort()
    summit_set = set(summits)
    
    # 인풋을 무방향 그래프로 변형
    graph = defaultdict(list)
    for i, j, w in paths:
        graph[i].append((w, j))
        graph[j].append((w, i))
        
    hq = []
    
    # visited의 초기값을 제약조건보다 1큰 값으로 해준다
    visited = [10000001] * (n+1)
    
    # 모든 출입구를 우선순위큐에 삽입한다
    for gate in gates:
        heappush(hq, (0, gate))
        visited[gate] = 0
        
    # intensity를 기준으로 다익스트라 진행
    while hq:
        intensity, node = heappop(hq)
        # 해당 노드의 방문경로가 intensity보다 작거나 정상노드이면 생략(continue)
        if intensity > visited[node] or node in summit_set:
            continue   
        for weight, next_node in graph[node]:
            next_intensity = max(weight, intensity)
            if next_intensity < visited[next_node]:
                # 다익스트라 진행 중 각 노드에 도달하는 과정의 최대 intensity값을 저장
                visited[next_node] = next_intensity
                heappush(hq, (next_intensity, next_node))
                
    # 다익스트라 완료 후 산봉우리들을 순회하며 정답을 찾는다
    min_intensity = [0, 10000001]
    for summit in summits:
        if min_intensity[1] > visited[summit]:
            min_intensity[0] = summit
            min_intensity[1] = visited[summit]
            
    return min_intensity
            
    
    
    