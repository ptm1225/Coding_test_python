import heapq
import sys
input = sys.stdin.readline

n = int(input())
plus = []
minus = []
for _ in range(n):
    i = int(input())
    if i > 0:
        heapq.heappush(plus, i)
    elif i < 0:
        heapq.heappush(minus, -i)
    else:
        if plus and minus:
            a = heapq.heappop(plus)
            b = -heapq.heappop(minus)
            if abs(a) >= abs(b):
                heapq.heappush(plus, a)
                print(b)
            elif abs(a) < abs(b):
                heapq.heappush(minus, -b)
                print(a)
        elif plus:
            print(heapq.heappop(plus))
        elif minus:
            print(-heapq.heappop(minus))
        else:
            print(0)