n = int(input())
m = int(input())
s = input()

t = 'IO'*n + 'I'

count = 0
for i in range(m-2*n):
    if t == s[i:i+(2*n+1)]:
        count += 1
print(count)