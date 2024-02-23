from math import sqrt
xa, ya, xb, yb, xc, yc = map(int, input().split())

if xa==xb==xc or ya==yb==yc or (xa-xb != 0 and xa-xc != 0 and xb-xc != 0 and (ya-yb)/(xa-xb) == (ya-yc)/(xa-xc) == (yb-yc)/(xb-xc)):
    print(-1.0)

else:
    arr = []
    
    # ac, bc
    arr.append(2*(sqrt((xa-xc)**2 + (ya-yc)**2) + sqrt((xb-xc)**2 + (yb-yc)**2)))
    # ab, bc
    arr.append(2*(sqrt((xa-xb)**2 + (ya-yb)**2) + sqrt((xb-xc)**2 + (yb-yc)**2)))
    # ab, ac
    arr.append(2*(sqrt((xa-xb)**2 + (ya-yb)**2) + sqrt((xa-xc)**2 + (ya-yc)**2)))
    
    print(max(arr)-min(arr))