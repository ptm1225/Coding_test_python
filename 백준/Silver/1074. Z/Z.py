n, r, c = map(int, input().split())
answer = 0
t = 2 ** (2*(n-1))
size = 2 ** (n-1)
for _ in range(n):
    if r < size and c < size:
        answer += 0
    elif r < size and c >= size:
        c -= size
        answer += t
    elif r >= size and c < size:
        r -= size
        answer += 2*t
    elif r >= size and c >= size:
        r -= size
        c -= size
        answer += 3*t
    size//=2
    t//=4
print(answer)