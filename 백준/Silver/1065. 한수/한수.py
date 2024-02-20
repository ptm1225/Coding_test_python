n = int(input())
result = 0

for number in range(1, n+1):
    s = list(map(int, str(number)))

    if len(s) < 3 or s[0]-s[1] == s[1]-s[2]:
        result += 1

print(result)