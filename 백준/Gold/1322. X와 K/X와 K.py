X, K = map(int, input().split())

a = []

while K > 1:
    a.append(K % 2)
    K //= 2
if K == 1:
    a.append(K)

i = 0
while X > 1:
    if X % 2 == 1:
        a.insert(i, 0)
    X //= 2
    i += 1
    
if X == 1:
    a.insert(i, 0)

result = 0
t = 1
for i in a:
    result += i*t
    t *= 2

print(result)