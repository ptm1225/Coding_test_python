while True:
    try:
        s, t = map(list, input().split())
        s = s[::-1]
        for x in t:
            if s and s[-1] == x:
                s.pop()
        print('Yes' if not s else 'No')
    except:
        break