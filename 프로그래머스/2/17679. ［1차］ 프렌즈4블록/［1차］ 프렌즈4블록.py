def solution(m, n, board):
    board = [list(x) for x in board]
    cnt = 0
    while True:
        d = set()
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] != '0' and board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1]:
                    for x in range(i, i+2):
                        for y in range(j, j+2):
                            d.add((x, y))
        if not d:
            break
        
        for x, y in d:
            if board[x][y] != '0':
                board[x][y] = '0'
                cnt += 1
        
        for i in range(m-1):
            for j in range(n):
                if board[i+1][j] == '0':
                    for k in range(i, -1, -1):
                        board[k][j], board[k+1][j] = '0', board[k][j]
    return cnt