def solution(order):
    main = 1
    sub = []
    count = 0
    for c in order:
        if c >= main:
            sub += list(range(main, c))
            main = c+1
            count += 1
        elif c == sub[-1]:
            sub.pop()
            count += 1
        else:
            break
    return count