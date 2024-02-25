from collections import Counter
s = dict(sorted(Counter(input()).items()))

result = []
f = []
for k, v in s.items():
    for _ in range(v//2):
        result.append(k)
        s[k] -= 2
    
    if s[k] == 1:
        f.append(k)

if len(f) > 1:
    print("I'm Sorry Hansoo")
if sum(s.values()) == 0:
    print(''.join(result + result[::-1]))
elif sum(s.values()) == 1:
    print(''.join(result + f + result[::-1]))