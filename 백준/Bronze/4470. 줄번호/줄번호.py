import sys
input = sys.stdin.readline

N = int(input())
arr = [input().rstrip() for _ in range(N)]
i = 1
for x in arr:
    print(f"{i}. {x}")
    i += 1