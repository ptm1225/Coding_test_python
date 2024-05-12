n = int(input())
arr = []
result = []

def dfs():
    if len(arr) > 0:
        result.append(int("".join(map(str, arr))))
        
    for i in range(10): 
        if len(arr) == 0 or arr[-1] > i:
            arr.append(i)
            dfs()
            arr.pop()

dfs()
result.sort()
if n < len(result):
    print(result[n])
else:
    print(-1)