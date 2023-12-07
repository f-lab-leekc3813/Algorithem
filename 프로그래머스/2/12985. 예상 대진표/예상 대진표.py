def solution(n,a,b):
    answer = 0
    # dfs?
    def dfs(a,b):
        # 짝수일때와 홀수일때의 track이 다르다.
        print(a,b)
        if a % 2 == 0:
            a_track = a/2
        else:
            a_track = (a+1) / 2
        if b % 2 == 0 :
            b_track = b / 2
        else:
            b_track = (b + 1) / 2
        if a_track == b_track:
            return 0
        else:
            return 1 + dfs(a_track, b_track)
            
    cnt = dfs(a,b)
    return cnt + 1