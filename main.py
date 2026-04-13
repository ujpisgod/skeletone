import ops as mm
a,b,c=map(int,input('3개의 숫자를 띄워쓰기해 입력해 주세요').split())
ma1=mm.create_r_mat(a,b)
for i in ma1:
    print(*i)
print(f'{a}곱하기 {b} 사이즈의 행렬입니다\n')
ma2=mm.create_r_mat(b,c)
for i in ma2:
    print(*i)
print(f'{b}곱하기 {c} 사이즈의 행렬입니다\n')
kk=mm.mat_mul(ma1,ma2)
print('\n 다음은 곱해진 행렬입니다 \n')
for i in kk:
    print(*i)
print('\n 곱한 행렬에 편향를 더합시다')
a2,b2=mm.ismat(kk)
fisrt_random=mm.create_r_mat(a2,b2)
tt=mm.mat_add(kk,fisrt_random)
for i in tt:
    print(*i)
print('\n 위 행렬은 랜덤 편향이 더해진 행렬입니다\n')
tt2=mm.relu(tt)
for i in tt2:
    print(*i)
print('\n 위 행렬은 랜덤 편향이 더해진 행렬이 레루 함수를 통과한 행렬입니다')