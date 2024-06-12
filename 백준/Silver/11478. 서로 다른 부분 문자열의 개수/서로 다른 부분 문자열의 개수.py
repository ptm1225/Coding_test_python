import sys
input = sys.stdin.readline

s = input().rstrip()
n = len(s)
arr = set()
for x in range(1, n+1):
    for i in range(n-x+1):
        arr.add(s[i:i+x])
print(len(arr))