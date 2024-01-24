def solution(n, words):
    past_words = []
    for i in range(len(words)):
        if words[i] in past_words:
            i -= 1
            break
        else:
            past_words.append(words[i])
            
    if i+1 != len(words):
        return [(i+1)%n + 1, (i+1)//n + 1]
    
    for i in range(len(words)-1):
        if past_words[i][-1] !=  words[i+1][0]:
            break
    
    if i+2 != len(words):
        return [(i+1)%n + 1, (i+1)//n + 1]
    else:
        return [0, 0]