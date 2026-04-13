import make_matrix as mm
a,b=map(int,input("행과 열의 크기를 입력하세요 (예: 3 4): ").split())
ma=mm.create_z_mat(a,b)
for i in ma:
    print(*i)