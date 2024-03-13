n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
answer = [0, 0]
def f(i, j, n):
    t = arr[i][j]
    if n == 1:
        answer[t] += 1
    else:
        for x in range(n):
            if (t+1)%2 in arr[i+x][j:j+n]:
                f(i, j, n//2)
                f(i, j+n//2, n//2)
                f(i+n//2, j, n//2)
                f(i+n//2, j+n//2, n//2)
                break
        else:
            answer[t] += 1
f(0, 0, n)
print(answer[0])
print(answer[1])