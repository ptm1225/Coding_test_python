n = int(input())
cups = [0] * 4
cups[1] = 1

for _ in range(n):
    a, b = map(int, input().split())
    cups[a], cups[b] = cups[b], cups[a]

print(cups.index(1))