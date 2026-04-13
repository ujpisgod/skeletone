def create_z_mat(a,b):
    l=[]
    for i in range(a):
        l.append([0]*b)
    return l
def mat_mul(a,b):
    if a and a[0]:
        n=len(a)
        k1=len(a[0])
    else:
        raise ValueError("1번 행렬이 비어있습니다.")
    if b and b[0]:
        k2=len(b)
        m=len(b[0])
    else:
        raise ValueError("2번 행렬이 비어있습니다.")
    if k1==k2:
        k=k1
    else:
        raise ValueError("행렬의 내항 차원이 일치하지 않습니다.")
    result=[[] for i in range(n)]
    for i in range(n):
        for j in range(m):
            d=0
            for x in range(k):
               d+=a[i][x]*b[x][j] 
            result[i].append(d)
    return result
