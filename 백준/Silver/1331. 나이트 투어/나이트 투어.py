arr = []
for _ in range(36):
    arr.append(input())

answer = 'Valid'

if len(set(arr)) != len(arr):
    answer = 'Invalid'

for i in range(36):
    alp = abs(ord(arr[i-1][0]) - ord(arr[i][0]))
    num = abs(int(arr[i-1][1]) - int(arr[i][1]))
    
    if (alp == 1 and num == 2) or (alp == 2 and num == 1):
        continue
    else:
        answer = 'Invalid'
        break

print(answer)