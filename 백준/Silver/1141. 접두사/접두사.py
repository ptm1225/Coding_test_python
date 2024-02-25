n = int(input())
arr = []
for _ in range(n):
    arr.append(input())

def f(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if i != j and arr[j].startswith(arr[i]):
                arr.pop(i)
                return arr
    return arr

arr.sort(key=lambda x:len(x))

while True:
    length = len(arr)
    arr = f(arr)
    if len(arr) == length:
        break

print(len(arr))