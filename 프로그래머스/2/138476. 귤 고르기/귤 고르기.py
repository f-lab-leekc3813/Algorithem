def solution(k, tangerine):
    answer = 0
    memo = {}
    for i in tangerine:
        if i not in memo:
            memo[i] = 1
        else:
            memo[i] += 1
    result_dic = sorted(memo.items(), key = lambda  item : item[1], reverse = True)
    for i in result_dic:
        answer += 1
        k -= i[1]
        if k <= 0:
            break
    return answer