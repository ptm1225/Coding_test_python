arr = []
for _ in range(int(input())):
    arr.append(int(input()))
num = [False] * (2*(10**6) + 1)
for a in arr:
    num[10**6 + a] = True

for i in range(-(10**6), (10**6) + 1):
    if num[10**6 + i]:
        print(i)