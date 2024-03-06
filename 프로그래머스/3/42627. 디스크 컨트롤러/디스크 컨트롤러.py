def solution(jobs):
    jobs.sort(key=lambda x:x[1])
    n = len(jobs)
    time = 0
    works = []
    answer = 0
    
    while works or jobs:
        for job in jobs:
            if job[0] <= time:
                works.append(job)
                jobs.remove(job)
        
        if works:
            works[0][1] -= 1
            if works[0][1] == 0:
                end = works.pop(0)
                answer += (time+1) - end[0]
                works.sort(key=lambda x:x[1])
        time += 1
    
    return int(answer / n)