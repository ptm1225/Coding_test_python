L = int(input())
S = set(map(int, input().split()))
n = int(input())
count = 0

for i in range(1, max(S)):
    for j in range(i+1, max(S)+1):
        if i <= n <= j:
            if set(range(i, j+1)) & S:
                continue
            else:
                count += 1

print(count)