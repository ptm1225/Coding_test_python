t = int(input())
for _ in range(t):
    n, s = input().split()
    print(''.join([int(n) * i for i in s]))