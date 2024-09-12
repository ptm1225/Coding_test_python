n = int(input())
arr = [0] * n

def bt(s, cnt):
    if cnt == n:
        print(*s)
        return
    
    for i in range(n):
        if not arr[i]:
            arr[i] = 1
            s.append(i+1)
            bt(s, cnt+1)
            s.pop()
            arr[i] = 0

bt([], 0)