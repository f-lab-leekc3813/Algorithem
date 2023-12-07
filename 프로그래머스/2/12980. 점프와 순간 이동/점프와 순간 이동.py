def solution(n):
    ans = 0
    # 현재위치 1
    cur_step = 1
    if n == 2:
        return 1
    if n == 1:
        return 1
    
    while(n>2):
        # n이 2로 나누어 떨어지면 카운트를 안올리고 2로 나눈다
        if n % 2 == 0:
            n = n / 2
        else:
            ans += 1
            n -= 1
    if n == 2 :
        ans += 1
        
    return ans