while True:
    try:
        R_C = input()
        while R_C.strip() == '':
            R_C = input()
        R, C = map(int, R_C.strip().split())
        if R == 0 and C == 0:
            break
        grid = []
        for _ in range(R):
            row = input()
            while len(row.strip()) == 0:
                row = input()
            grid.append(list(row.strip()))
        result = [['' for _ in range(C)] for _ in range(R)]
        for i in range(R):
            for j in range(C):
                if grid[i][j] == '*':
                    result[i][j] = '*'
                else:
                    count = 0
                    for dx in [-1, 0, 1]:
                        for dy in [-1, 0, 1]:
                            if dx == 0 and dy == 0:
                                continue
                            nx, ny = i + dx, j + dy
                            if 0 <= nx < R and 0 <= ny < C:
                                if grid[nx][ny] == '*':
                                    count +=1
                    result[i][j] = str(count)
        for row in result:
            print(''.join(row))
    except EOFError:
        break
