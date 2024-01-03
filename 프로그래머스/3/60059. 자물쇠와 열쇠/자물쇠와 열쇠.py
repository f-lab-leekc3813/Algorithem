# # 90도 회전하는 코드
# def rotate_90_degrees(matrix):
#     transposed_matrix = [list(row) for row in zip(*matrix)]
    
#     rotated_matrix = [list(reversed(row)) for row in transposed_matrix]
    
#     return rotated_matrix

# def attach(x, y, M, key, board):
#     for i in range(M):
#         for j in range(M):
#             board[x+i][y+j] += key[i][j]

# def detach(x, y, M, key, board):
#     for i in range(M):
#         for j in range(M):
#             board[x+i][y+j] -= key[i][j]

# def check(board, M, N):
#     for i in range(N):
#         for j in range(N):
#             if board[M+i][M+j] != 1:
#                 return False;
#     return True

# def solution(key, lock):
#     num_key = 0
#     num_lock = 0
#     # 열쇠의 돌기와 자물쇠의 홈 개수 비교
#     for i in key:
#         for j in i:
#             if j == 1:
#                 num_key += 1
#     for i in lock:
#         for j in i:
#             if j == 0:
#                 num_lock += 1
#     if num_key < num_lock:
#         return False
#     M,N = len(key), len(lock)
    
#     board = [[0] * (M*2 + N) for _ in range(M*2 + N)]
    
#     # lock 중앙 배치
#     for i in range(N):
#         for j in range(N):
#             board[M+i][N+j] = lock[i][j]
#     rotated_key = key
    
#     # 모든방향으로 key루프
    
#     for _ in range(4):
#         rotated_key = rotate_90_degrees(rotated_key)
#         for x in range(1, M+N):
#             for y in range(1,M+N):
#                 #열쇠 넣어보기
#                 attach(x, y, M, rotated_key, board)
#                 if(check(board, M, N)):
#                     return True
#                 # 열쇠 빼기
#                 detach(x, y, M, rotated_key, board)
    
    
#     return False

def attach(x, y, M, key, board):
    for i in range(M):
        for j in range(M):
            board[x+i][y+j] += key[i][j]

def detach(x, y, M, key, board):
    for i in range(M):
        for j in range(M):
            board[x+i][y+j] -= key[i][j]

def rotate90(arr):
    return list(zip(*arr[::-1]))

def check(board, M, N):
    for i in range(N):
        for j in range(N):
            if board[M+i][M+j] != 1:
                return False;
    return True

def solution(key, lock):
    M, N = len(key), len(lock)

    board = [[0] * (M*2 + N) for _ in range(M*2 + N)]
    # 자물쇠 중앙 배치
    for i in range(N):
        for j in range(N):
            board[M+i][M+j] = lock[i][j]

    rotated_key = key
    # 모든 방향 (4번 루프)
    for _ in range(4):
        rotated_key = rotate90(rotated_key)
        for x in range(1, M+N):
            for y in range(1, M+N):
                # 열쇠 넣어보기
                attach(x, y, M, rotated_key, board)
                # lock 가능 check
                if(check(board, M, N)):
                    return True
                # 열쇠 빼기
                detach(x, y, M, rotated_key, board)
                
    return False