while True:
    B, N = map(int, input().split())
    if B == N == 0:
        break
    a = int(B ** (1/N))
    print(a if abs(B-a**N) < abs(B-(a+1)**N) else a+1)