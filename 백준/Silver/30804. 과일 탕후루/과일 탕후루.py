import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

i = 0
result = 0
count = defaultdict(int)

for j in range(n):
    count[arr[j]] += 1

    while len(count) > 2:
        count[arr[i]] -= 1
        if count[arr[i]] == 0:
            del count[arr[i]]
        i += 1

    result = max(result, j - i + 1)

print(result)