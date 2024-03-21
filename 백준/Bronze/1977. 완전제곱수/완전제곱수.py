n = int(input())
m = int(input())
result = []
for i in range(n, m+1):
    if i**0.5 == int(i**0.5):
        result.append(i)
if result:
    print(sum(result))
    print(min(result))
else:
    print(-1)