def solution(n, words):
    answer = []
    check = {}
    last_words = words[0][-1]
    # 맨 처음 방문처리
    check[words[0]] = 1
    for i in range(1, len(words)):
        if words[i] not in check and last_words == words[i][0]:
            last_words = words[i][-1]
            check[words[i]] = 1
        else:
            return [i%n+1, i//n+1 ]
        
    return [0,0]