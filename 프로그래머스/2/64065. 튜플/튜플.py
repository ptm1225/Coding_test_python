def solution(s):
    ans = []
    arr = [list(map(int, i.lstrip('{').rstrip('}').split(','))) for i in s.split('},{')]
    arr.sort(key=lambda x:len(x))
    for i in arr:
        for x in ans:
            if x in i:
                i.remove(x)
        ans.append(*i)
    return ans