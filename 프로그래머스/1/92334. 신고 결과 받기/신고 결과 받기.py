def solution(id_list, report, k):
    answer = []
    # 누가 신고했는지 메모
    memo_report = {}
    
    # 신고 당한 횟수 메모
    memo_me = {}
    
    for char in report:
        # 신고한사람, 신고당한사람
        to, reporter = char.split(' ')
        # 처음 신고한 상황이면
        if to not in memo_report:
            memo_report[to] = [reporter]
        else:
            tmp = memo_report[to]
            tmp.append(reporter)
            a = set(tmp)
            memo_report[to] = list(a)
            
        # 누가 신고당했는지
        if reporter not in memo_me:
            memo_me[reporter] = [to]
        else:
            tmp = memo_me[reporter]
            tmp.append(to)
            a = set(tmp)
            memo_me[reporter] = list(a)
    
    stop_users = {}
    for i in memo_me:
        # 정지대상이면 stop_user에 넣어준다
        if len(memo_me[i]) >= k:
            stop_users[i] = 1

    
    for i in id_list:
        now_cnt = 0
        if i in memo_report:
            cur_value = memo_report[i]
            
            for j in cur_value:
                if j in stop_users:
                    now_cnt += 1
        answer.append(now_cnt)
    
    
    return answer