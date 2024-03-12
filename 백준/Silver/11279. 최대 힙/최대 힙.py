import heapq
import sys
input = sys.stdin.readline

n = int(input())
arr = []
result = []
for _ in range(n):
    x = int(input())
    if x > 0:
        heapq.heappush(arr, -x)
    else:
        if arr:
            result.append(-heapq.heappop(arr))
        else:
            result.append(0)
for r in result:
    print(r)