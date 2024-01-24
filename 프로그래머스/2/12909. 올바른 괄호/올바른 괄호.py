def solution(s):
    answer = True
    n = []
    for w in s:
        if len(n) == 0 or w == '(':
            n.append(w)
        else:
            if n[-1] == '(':
                n.pop()
            else:
                n.append(w)
    return True if len(n) == 0 else False