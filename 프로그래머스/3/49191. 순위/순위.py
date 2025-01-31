def solution(n, results):
    graph = [[0] * (n + 1) for _ in range(n + 1)]
    
    for win, lose in results:
        graph[win][lose] = 1
        graph[lose][win] = -1
    
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1
                    graph[j][i] = -1
                elif graph[i][k] == -1 and graph[k][j] == -1:
                    graph[i][j] = -1
                    graph[j][i] = 1
    
    count = 0
    for i in range(1, n + 1):
        if graph[i][1:].count(0) == 1:
            count += 1

    return count