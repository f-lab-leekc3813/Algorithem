def solution(clothes):
    hash_map = {}
    # 옷을 해시화
    for cloth, type in clothes:
        hash_map[type] = hash_map.get(type, 0) + 1
    # 아무것도 입지않은 경우를 추가
    answer = 1
    for type in hash_map:
        answer *= (hash_map[type] + 1)
    
    
    return answer - 1