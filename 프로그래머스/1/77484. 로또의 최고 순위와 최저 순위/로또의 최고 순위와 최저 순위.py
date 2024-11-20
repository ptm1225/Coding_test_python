def solution(lottos, win_nums):
    cor = 0
    zero = 0
    for l in lottos:
        if l in win_nums:
            cor += 1
        elif l == 0:
            zero += 1
    
    return 7 - (cor + zero) if 7 - (cor + zero) < 7 else 6, 7 - cor if 7 - cor < 7 else 6