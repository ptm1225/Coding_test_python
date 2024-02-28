n = int(input())
arr = []
for _ in range(n):
    arr.append(input())

length = len(arr[0])
answer = 0

for k in range(-1, -(length+1), -1):
    s = []
    for i in range(n):
        s.append(arr[i][-1:k-1:-1])
    if len(s) == len(set(s)):
        answer = -k
        break

print(answer)