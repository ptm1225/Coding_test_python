from copy import deepcopy
import sys
input = sys.stdin.readline

s = input().rstrip()
arr = []
t = [0] * 26
for i, v in enumerate(s):
    t[ord(v)-97] += 1
    arr.append(deepcopy(t))
q = int(input())
for _ in range(q):
    al, l, r = input().split()
    l = int(l)
    r = int(r)
    print(arr[r][ord(al)-97] - arr[l-1][ord(al)-97] if l > 0 else arr[r][ord(al)-97])