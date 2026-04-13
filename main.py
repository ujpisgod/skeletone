import ops as mm
a,b=map(int,input("첫번째 행렬의 행과 열의 크기를 입력하세요 (예: 3 4): ").split())
ma1=mm.create_z_mat(a,b)
for i in ma1:
    print(*i)
a,b=map(int,input("두번째 행렬의 행과 열의 크기를 입력하세요 (예: 3 4): ").split())
ma2=mm.create_z_mat(a,b)
for i in ma2:
    print(*i)
kk=mm.mat_mul(ma1,ma2)
print('\n')
for i in kk:
    print(*i)