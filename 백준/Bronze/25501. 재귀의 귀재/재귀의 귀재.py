t = int(input())
def recursion(s, left, right, cnt):
    cnt += 1
    if left >= right:
        return (1, cnt)
    elif s[left] != s[right]:
        return (0, cnt)
    else:
        return recursion(s, left+1, right-1, cnt)

for _ in range(t):
    s = input()
    print(*recursion(s, 0, len(s)-1, 0))