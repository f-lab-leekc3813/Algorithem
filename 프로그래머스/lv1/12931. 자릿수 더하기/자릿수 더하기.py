def solution(n):
    answer = 0

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.

    str_n = str(n)
    for i in str_n:
        answer += int(i)
    return answer