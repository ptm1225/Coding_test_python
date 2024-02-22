def solution(dirs):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    a = ['L','R','U','D']
    visited = []
    x, y = 5, 5
    count = 0
    
    for d in dirs:
        for i in range(len(a)):
            if a[i] == d:
                tmp_x, tmp_y = x, y
                x += dx[i]
                y += dy[i]
                if x < 0 or y < 0 or x > 10 or y > 10:
                    x, y = tmp_x, tmp_y
                    break
                else:
                    move = ((tmp_x, tmp_y), (x, y))
                    move_reversed = ((x, y), (tmp_x, tmp_y))
                    if move not in visited and move_reversed not in visited:
                        visited.append(move)
                        count += 1
    return count