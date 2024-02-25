def is_pelin(s):
    return s[:len(s)//2] == s[-1:-(len(s)//2+1):-1]

s = list(input())
result = []
for i in range(1, len(s)+1):
    new_s = s + s[-(i+1):-len(s)-1:-1]
    if is_pelin(new_s):
        result.append(new_s)

result.sort(key=lambda x:len(x))

print(len(result[0]))