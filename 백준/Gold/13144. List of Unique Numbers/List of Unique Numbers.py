N = int(input())
A = list(map(int, input().split()))

cnt = 0
i, j = 0, 0
s = set()

while j < N:
    if A[j] not in s:
        s.add(A[j])
        j += 1
    else:
        cnt += j - i
        s.remove(A[i])
        i += 1

cnt += (j-i) * (j-i+1) // 2

print(cnt)