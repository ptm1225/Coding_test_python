m, s = map(int, input().split())
p = int(input())
print((m+(s+p)//60)%24, (s+p)%60)