def solution(x):
    return x % eval('+'.join(t for t in str(x))) == 0