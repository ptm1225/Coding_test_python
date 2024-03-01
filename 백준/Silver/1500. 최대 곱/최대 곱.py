s, k = map(int, input().split())
result = []
n = k - 1
for i in range(n):
    result.append(s//k)
    s -= s//k
    k -= 1

result.append(s)

print(eval('*'.join(map(str,result))))