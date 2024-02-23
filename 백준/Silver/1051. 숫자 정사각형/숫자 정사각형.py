n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(input())

answer = []
for l in range(min(n, m)):
    for i in range(n-l):
        for j in range(m-l):
            if arr[i][j] == arr[i+l][j] == arr[i][j+l] == arr[i+l][j+l]:
                answer.append((l+1)**2)
if answer:
    print(max(answer))
else:
    print(1)