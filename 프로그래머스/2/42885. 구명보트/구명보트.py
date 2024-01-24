def solution(people, limit):
    people.sort()
    front, rear = 0, len(people) - 1
    count = 0
    while front <= rear:
        if limit >= people[front] + people[rear]:
            front += 1
        rear -= 1
        count += 1
    return count