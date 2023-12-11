def solution(s):
    answer = []
    dic_map = {}
    result = [[int(num) for num in inner_list.split(',') if num] for inner_list in s.strip('{}').split('},{')]
    sorted_result = sorted(result, key = len)
    
    for i in sorted_result:
        for k in i:
            if k not in dic_map:
                dic_map[k] = 1
                answer.append(k)
                break
    
    return answer