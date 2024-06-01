import sys
input = sys.stdin.readline

n = int(input())
road = list(map(int, input().split()))
oil = list(map(int, input().split()))

p = 10 ** 12
w = 0

for i in range(n-1):
    p = min(p, oil[i])
    w += p * road[i]
print(w)