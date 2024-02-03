import heapq

def solution(n, s, a, b, fares):
		#✅ 인풋을 본인이 쓰기 편한 구조로 바꾸기(다익스트라) => 무방향 그래프 만들기
    graph = [[] for _ in range(n+1)]
    for u, v, w in fares:
        graph[u].append((v,w))
        graph[v].append((u,w))

    answer = 100000000

		#✅ s, a, b 3개의 노드에서 모든 노드까지 도달하는 최소 비용을 저장한다.
    costs = [[100000000 for _ in range(n+1)] for _ in range(3)]
    
		#✅ s, a, b 3개의 노드에서 각각 다익스트라 알고리즘을 수행한다.
    for i, start_node in enumerate([s, a, b]):
        heap = []
        heapq.heappush(heap, (0, start_node))
        costs[i][start_node] = 0

        while heap:
            cur_cost, cur_v = heapq.heappop(heap)
            for next_v, cost in graph[cur_v]:
                next_cost = cur_cost+cost
                if costs[i][next_v] > next_cost:
                    costs[i][next_v] = next_cost
                    heapq.heappush(heap, (next_cost, next_v))

		#✅ 모든 노드를 순회하며 cost(s->x) + cost(x->a) + cost(x->b)의 최소비용을 반환한다.
    for i in range(1, n+1):
        answer = min(answer, costs[0][i]+costs[1][i]+costs[2][i])
    return answer