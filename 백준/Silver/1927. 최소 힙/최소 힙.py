import heapq
n = int(input())
seq = []
for _ in range(n):
    seq.append(int(input()))

arr = []
for inp in seq:
    if inp == 0:
        if arr:
            print(heapq.heappop(arr))
        else:
            print(0)
    else:
        heapq.heappush(arr, inp)