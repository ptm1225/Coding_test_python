from itertools import permutations
n = int(input())
x = list(map(int, input().split()))
result = 0

for arr in permutations(x, n):
    cnt = 0
    for i in range(n):
        s = 0
        j = i
        while s <= 50:
            s += arr[j]
            if s == 50:
                cnt += 1
                break
            j = (j+1) % n
    result = max(result, cnt//2)
print(result)