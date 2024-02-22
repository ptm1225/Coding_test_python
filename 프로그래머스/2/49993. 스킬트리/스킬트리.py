def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        stack = []
        for t in tree:
            if t in skill:
                stack.append(t)
        is_pos = True
        for i,v in enumerate(stack):
            if skill[i] != v:
                is_pos = False
                break
        if is_pos:
            answer += 1
    return answer