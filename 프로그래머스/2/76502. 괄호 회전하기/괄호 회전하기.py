from collections import deque

def solution(s):
    answer = 0
    
    if len(s) == 1:
        return 0
    
    for i in range(len(s)):
        queue = deque(s)
        # check_num이 1이면 괄호유효 0이면 유효 x
        check_num = 1
        # 회전하고 괄호 유효성검사 popleft를 i 개수만큼하고 append해준다
        for j in range(i):
            tmp = queue.popleft()
            queue.append(tmp)
        # 횟수마다 회전 완료 괄호 유효성검사
        stack = []
        for k in queue:
            if k == '[':
                stack.append(']')
            elif k == '{':
                stack.append('}')
            elif k == '(':
                stack.append(')')
            else:
                if len(stack) == 0:
                    check_num = 0
                    break
                elif stack.pop() != k:
                    check_num = 0
                    break
        if check_num == 1 and len(stack) == 0:
            answer += 1
        
    return answer