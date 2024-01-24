def solution(s):
    arr = []
    words = s.split(' ')
    for word in words:
        if '-' in word:
            word = word[1::]
            arr.append(int(word) * -1)
        else:
            arr.append(int(word))
    arr.sort()
    answer = str(arr[0]) + ' ' + str(arr[-1])
    return answer