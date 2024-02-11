from collections import deque

def solution(n, computers):
    visited = [False] * n
    q = deque()
    count = 0
    
    for s in range(n):
        if all(visited):
            break
        
        if visited[s]:
            continue
        else:
            q.append(s)
            visited[s] = True
            while q:
                v = q.popleft()
                for i in range(n):
                    if computers[v][i] == 1 and v != i:
                        q.append(i)
                        computers[v][i] += 1
                        computers[i][v] += 1
                        visited[i] = True
            count += 1
    return count