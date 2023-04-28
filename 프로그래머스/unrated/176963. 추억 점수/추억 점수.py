def solution(name, yearning, photo):
    answer = []
    name_dic = {}
    for i in range(len(name)):
        name_dic[name[i]] = yearning[i]
    for i in photo:
        sum = 0
        for j in i:
            if j in name_dic:
                sum += name_dic[j]
        answer.append(sum)
    return answer