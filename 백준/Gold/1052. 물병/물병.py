import sys
input = sys.stdin.readline

n, k = map(int, input().split())
count = 0

while bin(n).count('1') > k:
    i = bin(n)[::-1].index('1')
    n += 2 ** i
    count += 2 ** i

print(count)