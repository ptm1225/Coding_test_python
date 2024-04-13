n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
t = 0
left = 0
right = 0
for x in arr:
    if x > t:
        t = x
        left += 1
t = 0
for x in arr[::-1]:
    if x > t:
        t = x
        right += 1

print(left)
print(right)