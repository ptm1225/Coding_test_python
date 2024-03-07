t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    q = list(map(int, input().split()))
    idx = list(range(n))
    count = 0
    while q:
        if len(q) == 1:
            count += 1
            break
        
        elif q[0] < max(q[1:]):
            q.append(q.pop(0))
            idx.append(idx.pop(0))
        else:
            q.pop(0)
            count += 1
            if idx.pop(0) == m:
                break
        
    print(count)