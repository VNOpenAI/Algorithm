
'''
B1:
    tìm dãy con đối xứng dài nhất
    ví dụ  1 2 8 2 5 2 2 1
        =>  1 2 2 5 2 2 1
        f[i][j] là độ dài của xâu con đói xứng dài nhất từ i => j
        kết quả bài toán f[0][n-1]
        f[i][j]
            f[i-1,...0][:]
            f[:][j-1]

            nếu a[i]==a[j]=>f[i][j]=f[i+1][j-1]+2
            ngược lại => max(f[i][j-1],f[i+1][j])
'''

a = [1, 2, 8, 2, 5, 2, 2, 1]
n = len(a)
f = []
for i in range(n):
    f.append([])
    for j in range(n):
        f[i].append(0)

# f = [[0]*n]*n # error vì các phần tử đều tham chiếu tới 1 phần tử. khi 1 phần tử thay đổi thì
# các phần tử khác thay đổi theo
    # range(a,b,c) = > bắt đầu từ a => b-c

# xử lí i==j
for i in range(n):
    f[i][i] = 1

# i=n-1 => j=n-1 f[n-1][n-1]=1
# j=0=>i=0 => f[0][0]=1

# a=[1,2,8,2,5,2,2,1]

for i in range(n-2, -1, -1):
    for j in range(i+1, n):
        if(a[i] == a[j]):
            f[i][j] = f[i+1][j-1]+2
        else:
            f[i][j] = max(f[i][j-1], f[i+1][j])

# vấn đề là không có f[:][-1], f[n][:] => j!=0,i!=n-1
# xử lí j=0,i=n-1 ,i==j
# print(f[0][n-1])


res = []
while i <= j:
    if a[i] == a[j]:
        res.append(a[i])
        i += 1
        j -= 1
    else:
        if f[i][j-1] > f[i+1][j]:
            j -= 1
        else:
            i += 1

res = res + res[:(f[0][n-1]-len(res))][::-1]
print(*res, sep=' ')


'''
B2 tìm độ dài dãy con chung dài nhất 
    A : 1 3 2 5 6 3 2 2 3 
    B : 0 1 2 0 6 2 5
    => 1 2 6 2

    f[i][j] : là độ dài dãy con chung dài nhất của a[0->i] và b[0->j]
    output bài toán : f[n-1][m-1]
    f[i][j]= 
        a[i]==b[j] : f[i][j]=f[i-1][j-1]+1
        else : max(f[i-1][j],f[i][j-1])
'''
a = [1, 3, 2, 5, 6, 3, 2, 2, 3]
b = [0, 1, 2, 0, 6, 2, 5]
# 1 2 6 2
n = len(a)
m = len(b)

f = []
for i in range(n):
    f.append([])
    for j in range(m):
        f[i].append(0)

# xet i=0,j=0
if(a[0] == b[0]):
    f[0][0] = 1

# xet i =0
for j in range(1, m):
    if(a[0] == b[j]):
        f[0][j] = 1
    else:
        f[0][j] = f[0][j-1]

# xet j =0
for i in range(1, n):
    if(a[i] == b[0]):
        f[i][0] = 1
    else:
        f[i][0] = f[i-1][0]


for i in range(1, n):
    for j in range(1, m):
        if(a[i] == b[j]):
            f[i][j] = f[i-1][j-1]+1
        else:
            f[i][j] = max(f[i-1][j], f[i][j-1])

res = []
while(i >= 0 and j >= 0):
    if(a[i] == b[j]):
        res.append(a[i])
        i -= 1
        j -= 1
    else:
        if(f[i][j-1] > f[i-1][j]):
            j -= 1
        else:
            i -= 1

print(*res[::-1], sep=' ')
