from copy import deepcopy

arr = []
answer = 0

r, c, k = map(int, input().split())
for _ in range(r):
    arr.append(list(input()))

def func(i, j, arr, step):
    if not (i < 0 or j < 0 or i > len(arr)-1 or j > len(arr[0])-1 or arr[i][j] == 'T') and arr[i][j] == '.':
        
        if i == 0 and j == len(arr[0])-1:
            global k, answer
            if step == k:
                answer += 1
        
        arr[i][j] = step
        tmp1, tmp2, tmp3, tmp4 = deepcopy(arr), deepcopy(arr), deepcopy(arr), deepcopy(arr)
        func(i-1, j, tmp1, step+1)
        func(i+1, j, tmp2, step+1)
        func(i, j-1, tmp3, step+1)
        func(i, j+1, tmp4, step+1)

func(r-1, 0, arr, 1)

print(answer)