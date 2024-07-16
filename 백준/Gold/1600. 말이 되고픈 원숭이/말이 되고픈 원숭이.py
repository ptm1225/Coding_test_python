from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    q = deque([(0, 0, K)])
    visited = [[-1] * W for _ in range(H)]
    visited[0][0] = K
    cnt = 0

    while q:
        for _ in range(len(q)):
            i, j, k = q.popleft()
            if i == H-1 and j == W-1:
                return cnt
            for x, y in d:
                ni, nj = i + x, j + y
                if 0 <= ni < H and 0 <= nj < W and visited[ni][nj] < k and arr[ni][nj] == 0:
                    visited[ni][nj] = k
                    q.append((ni, nj, k))
            if k > 0:
                for x, y in h:
                    ni, nj = i + x, j + y
                    if 0 <= ni < H and 0 <= nj < W and visited[ni][nj] < k - 1 and arr[ni][nj] == 0:
                        visited[ni][nj] = k - 1
                        q.append((ni, nj, k - 1))
        cnt += 1
    return -1

d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
h = [(2, 1), (2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]

K = int(input())
W, H = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(H)]

print(bfs())