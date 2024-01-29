def solution(s):
    result = 0
    d = {')':'(', '}':'{', ']':'['}
    for i in range(len(s)):
        s = s[1:] + s[0]
        arr = ['c']
        
        for v in s:
            if v in d.keys() and arr[-1] == d[v]:
                arr.pop()
            else:
                arr.append(v)
        result += 1 if len(arr) == 1 else 0
    return result