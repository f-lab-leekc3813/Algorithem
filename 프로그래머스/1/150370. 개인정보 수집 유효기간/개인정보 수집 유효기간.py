def solution(today, terms, privacies):
    answer = []
    year, month, day = today.split('.')
    dead_line = int(year) * 336 + int(month) * 28 + int(day)
    
    memo = {}
    
    for i in terms:
        plan, month = i.split(' ')
        memo[plan] = int(month) * 28
    
    for i, char in enumerate(privacies):
        # 날짜와 plan을 분리한다
        date, plan = char.split(' ')
        # 현재의 년, 월, 일을 분리한다
        cur_year, cur_month, cur_day = date.split('.')
        # 현재의 날짜를 일단위로 바꾼다
        cur_dates = int(cur_year) * 336 + int(cur_month) * 28 + int(cur_day)
        cur_answer = cur_dates + memo[plan]
        if cur_answer <= dead_line:
            answer.append(i+1)
        
        
    return answer