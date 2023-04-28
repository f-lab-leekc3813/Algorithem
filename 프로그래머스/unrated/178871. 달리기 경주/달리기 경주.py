def solution(players, callings):
    player_idx = {player: idx for idx, player in enumerate(players)}

    for i in callings:
        now_idx = player_idx[i]
        tmp = players[now_idx - 1]
        players[now_idx] = tmp
        players[now_idx - 1] = i
        player_idx[i] = now_idx - 1
        player_idx[tmp] = now_idx
    
    return players