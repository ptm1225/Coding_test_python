n = int(input())
inp = input()[::-1]
if n == 1:
    print(inp[0])
else:
    dic = {"AA" : "A", "AG" : "C", "AC" : "A", "AT" : "G", "GA" : "C",
           "GG" : "G", "GC" : "T", "GT" : "A", "CA" : "A", "CG" : "T",
           "CC" : "C", "CT" : "G", "TA" : "G", "TG" : "A", "TC" : "G",
           "TT" : "T"}
    
    x = inp[0]
    s = inp[1]
    for i in range(n-2):
        s = dic[x+s]
        x = inp[i+2]
    print(dic[s+x])