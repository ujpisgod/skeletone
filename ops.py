def create_z_mat(a,b):
    l=[]
    for i in range(a):
        l.append([0]*b)
    return l
def ismat(a):
    if a and a[0]:
        n=len(a)
        k1=len(a[0])
    else:
        raise ValueError("행렬이 비어있습니다.")
    return n,k1
def create_r_mat(a,b):
    import random
    l=[[] for _ in range(a)]
    for i in range(a):
        for j in range(b):
            l[i].append(random.uniform(-1, 1))
    return l
def mat_mul(a,b):
    aa,k1=ismat(a)
    k2,bb=ismat(b)
    if k1==k2:
        k=k1
    else:
        raise ValueError("행렬의 내항 차원이 일치하지 않습니다.")
    result=[[] for i in range(aa)]
    for i in range(aa):
        for j in range(bb):
            d=0
            for x in range(k):
               d+=a[i][x]*b[x][j] 
            result[i].append(d)
    return result
def mat_add(a,b):
    a1,a2=ismat(a)
    b1,b2=ismat(b)
    if a1==b1 and a2==b2:
        c=[[] for i in range(a1)]
        for i in range(a1):
            for j in range(a2):
                c[i].append(a[i][j]+b[i][j])
        return c
    else:
        raise ValueError('행과 열이 맞지 않는 행렬끼리는 더할 수 없습니다')
def mat_sub(a,b):
    a1,a2=ismat(a)
    b1,b2=ismat(b)
    if a1==b1 and a2==b2:
        c=[[] for i in range(a1)]
        for i in range(a1):
            for j in range(a2):
                c[i].append(a[i][j]-b[i][j])
        return c
    else:
        raise ValueError('행과 열이 맞지 않는 행렬끼리는 뺄 수 없습니다')
def relu(a):
    n,m=ismat(a)
    result=[[] for i in range(n)]
    for i in range(n):
        for j in range(m):
            result[i].append(max(0,a[i][j]))
    return result
def mat_sum_sq(a):
    d=0
    n,m=ismat(a)
    for i in range(n):
        for j in range(m):
            d+=a[n][m]**2
    return d