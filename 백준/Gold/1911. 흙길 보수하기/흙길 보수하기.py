N, L = map(int,input().split())

lst = [list(map(int,input().split())) for _ in range(N)]

lst.sort()
cnt =0  

for pool in range(len(lst)) :
    length = lst[pool][1]-lst[pool][0]
    if pool == len(lst)-1 :
        cnt +=  (length-1)//L +1
        break
    if (length)% L  :
        tmp = L - ((length)% L)
        now_corver = lst[pool][1] + tmp 
        if lst[pool+1][0] <=now_corver : 
            lst[pool+1][0] = now_corver
        cnt += (length)//L +1
    else : 
        cnt += (length)//L 
print(cnt)