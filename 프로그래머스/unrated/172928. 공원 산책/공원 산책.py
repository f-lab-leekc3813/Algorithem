def solution(park, routes):
    answer = []
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == 'S':
                answer.append(i)
                answer.append(j)
                break
    for r in routes:
        x, y = answer[0], answer[1]
        d, steps = r.split(' ')
        dx, dy = 0, 0
        sw = 0
        if d == 'N':
            dx = -1
        elif d == 'S':
            dx = 1
        elif d == 'E':
            dy = 1
        else:
            dy = -1
        for _ in range(int(steps)):
            x, y = x + dx, y + dy
            if x < 0 or x >= len(park) or y < 0 or y >= len(park[0]) or park[x][y] == 'X':
                sw += 1
                break
                print(x,y)
        if sw == 0:
            answer[0], answer[1] = x, y
    return answer