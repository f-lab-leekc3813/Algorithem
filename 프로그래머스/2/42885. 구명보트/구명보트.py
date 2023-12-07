from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    # people를 순회하다가 같이탈수 없는 무게면 break
    # two point로 풀어보자
    # 맨 처음과 마지막에 포인트를 주고 
    queue = deque(people)
    start_point = 0
    end_point = len(queue) - 1
    
    # start_point와 end_point가 만날 때 까지
    while len(queue) > 1:
        if queue[start_point] + queue[end_point] > limit:
            answer += 1
            queue.pop()
            end_point -= 1
        else:
            queue.popleft()
            queue.pop()
            end_point -= 2
            answer += 1
    if len(queue) == 1:
        return answer + 1
    
    return answer