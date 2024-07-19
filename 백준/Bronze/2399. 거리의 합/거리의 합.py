import sys
input = sys.stdin.readline

n = int(input())
x = list(map(int, input().split()))

ans = 0
for i in range(n):
    for j in range(n):
        ans += abs(x[i]-x[j])

print(ans)