import heapq
n = int(input())
dasom = int(input())
if n == 1:
    print(0)
else:
    past = dasom
    other = []
    for _ in range(n-1):
        other.append(-int(input()))
    
    heapq.heapify(other)
    while True:
        m = -heapq.heappop(other)
        if dasom < m:
            dasom, m = dasom+1, m-1
            heapq.heappush(other,-m)
        else:
            if dasom == m:
                dasom += 1
            break
    print(dasom-past)