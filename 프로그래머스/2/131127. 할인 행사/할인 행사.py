from collections import deque

def solution(want, number, discount):
    answer = 0
    basket = []
    for i in range(len(want)):
        for k in range(number[i]):
            basket.append(want[i])
    # queue를 이용해서 풀어보자
    queue = deque()
    for item in discount:
        # queue와 basket의 길이가 같으면 큐업데이트
        if len(queue) == len(basket):
            queue.popleft()
            queue.append(item)
        else:
            queue.append(item)
        # 세일 항목수가 같으면
        if sorted(basket) == sorted(queue):
            answer += 1
        
    return answer