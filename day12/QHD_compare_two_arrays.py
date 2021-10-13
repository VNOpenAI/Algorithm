t1 = " Chị Thủy Xinh Gái"
t2 = "Chị Thủy xih gái ."
'''
Cần tìm số bước  thêm, sửa, xóa để  2 xâu giống hệt nhau
=> " Chị Thủy xinh Gái ."

gọi f[i][j]: số bước cần xử lý (xóa, thêm, sửa) ít nhất để 2 xâu giống nhau a[0:i] = b[0:j]
output f[n-1][m-1]
formula:
    * if a[i] == b[j]: f[i][j] = f[i-1][j-1]
    * else: 3 cases: 
        1. change a[i]/ b[j] 
            f[i-1][j-1] + 1
        2. delete a[i]/ b[j]
            min(f[i-1][j], f[i][j-1]) +1
        f[i][j] = min((f[i-1][j-1] + 1), (min(f[i-1][j], f[i][j-1]) +1))
'''

<<<<<<< HEAD
# Bài toán 1 : xóa (thêm)
# gọi f[i][j] số phần tử cần xóa ít nhất vào 2 xâu  để s[0-i] = s[0->j]
# output f[n-1][m-1]
# công thức : f[i][j]=f[i-1][j-1] nếu a[i]==a[j]
#             f[i][j]=min(f[i-1][j],f[i][j-1])+1


#bài toán 2 : sửa 
#gọi f[i][j] số phần tử cần sửa ít nhất vào 2 xâu  để s[0-i] = s[0->j]
# output f[n-1][m-1]
# công thức : f[i][j]=f[i-1][j-1] nếu a[i]==a[j]
#             f[i][j]=f[i-1][j-1]+1 nếu a[i]==a[j]






=======

def step(t1: str, t2: str):
    n = len(t1)
    m = len(t2)
    f = []
    for i in range(n):
        f.append([])
        for j in range(m):
            f[i].append(0)

    # initiate f[:][0] 
    # at 0, 0: min step is to change => f 00 = 1/ 0
    if t1[0] == t2[0]:
        f[0][0] = 0
    else:
        f[0][0] = 1

    # initiate f[:][0]
    for i in range(1, n):
        if t1[i] == t2[0]:
            f[i][0] = i
        else:
            f[i][0] = f[i-1][0]+1
    # initiate f[0][:]
    for j in range(1, m):
        if t1[0] == t2[j]:
            f[0][j] = j
        else:
            f[0][j] = f[0][j-1]+1

    for i in range(1, n):
        for j in range(1, m):
            if t1[i] == t2[j]:
                f[i][j] = f[i-1][j-1]
            else:
                f[i][j] = min((min(f[i-1][j], f[i][j-1]) + 1), (f[i-1][j-1]+1))
    print(f[n-1][m-1])


step(t1,t2)
>>>>>>> 6b362113038fc4ff03faf53aaadfd6e7bac29f57
