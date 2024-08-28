n = int(input())
A = list(map(int, input().split()))
ps = [0] * n
ps[0] = A[0]
for i in range(1, n):
    ps[i] = ps[i-1] + A[i]

result = 0
for i in range(n):
    result += (A[i] * (ps[-1] - ps[i]))
    result = result % 1000000007

print(result)