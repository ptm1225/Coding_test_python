n = int(input())
for _ in range(n):
    G = int(input())
    arr = [int(input()) for _ in range(G)]
    i = 1
    while True:
        t = [x%i for x in arr]
        if len(t) == len(set(t)):
            break
        i += 1
    print(i)