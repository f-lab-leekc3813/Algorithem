def solution(wallpaper):
    answer = []
    small_x = 0
    small_y = 0
    max_x = 0
    max_y = 0
    # 초기숫자세팅
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                small_x = i
                small_y = j
                max_x = i
                max_y = j
                break
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                small_x = min(i,small_x)
                small_y = min(j,small_y)
                max_x = max(i,max_x)
                max_y = max(j,max_y)
                
    answer.append(small_x)
    answer.append(small_y) 
    answer.append(max_x+1) 
    answer.append(max_y+1) 
    
    return answer