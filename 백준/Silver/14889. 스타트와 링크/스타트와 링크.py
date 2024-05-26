from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

visited = [False] * n
result = 10 ** 9
def f(s, cnt):
    if cnt == n//2:
        v = list(range(n))
        for i in s:
            v.remove(i)

        a = sum([arr[i][j] + arr[j][i] for i, j in combinations(s, 2)])
        b = sum([arr[i][j] + arr[j][i] for i, j in combinations(v, 2)])
        
        global result
        result = min(result, abs(a-b))
        
    else:
        for i in range(n):
            if cnt == 0 or (s and i > s[-1] and not visited[i]):
                s.append(i)
                visited[i] = True
                f(s, cnt+1)
                s.pop()
                visited[i] = False

f([], 0)
print(result)