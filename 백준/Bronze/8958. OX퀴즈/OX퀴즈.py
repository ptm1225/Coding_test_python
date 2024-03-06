for _ in range(int(input())):
    print(sum([len(i)*(len(i)+1)//2 for i in input().replace('X', ' ').split()]))