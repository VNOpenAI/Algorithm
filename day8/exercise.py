'''
bài 1:
o	Bài toán fibonaci F[i]=f[i-1]+f[i-2]
C1: dùng mảng f -> Tốn bộ nhớ
C2: dùng 3 biến f1, f2, f3
'''
# Solution 1:


def fibonaci1(n):
    f = [0, 1]
    for i in range(2, n):
        f.append(f[i-1]+f[i-2])
    print(f[-1])


fibonaci1(10)

# Solution 2:


def fibonaci2(n):
    f0, f1 = 0, 1
    for i in range(n-2):
        f2 = f0 + f1
        f0, f1 = f1, f2
    print(f2)


fibonaci2(10)

'''
Bài 2:
o	Bài toán tính tổng đoạn con
dãy số A 
k câu hỏi : tổng của dãy A[first ->last]?
VD: A = [1 ,5 ,6, 7,4,2,2,3]
tổng A[2->5]
Tổng A[4-7]
'''
A = [1, 5, 6, 7, 4, 2, 2, 3]


def totalsum(A):
    f = []
    s = 0
    for i in range(len(A)):
        s += A[i]
        f.append(s)
    return f


def subsum(f, first, last):
    print(f[last] - f[first-1])


f = totalsum(A)
subsum(f, 1, 3)


'''
# Bài 2:
# o	Bài toán tìm max dãy con từ index 0
# k câu hỏi ( mỗi câu hỏi nhận last => hỏi max (A[0->last])
# '''
A = [1, 5, 6, 7, 4, 2, 2, 3]

# f[i] : là max(A[0->i])
# 
# f[i]= max(f[i-1],a[i])# coong thức tổng quát
# 
# Max(A[0->Q]) : f[q] # kết quả bài toán
# 
# Phần tử neo : f[0]=a[0]

def totalmax(A):
    f=[A[0]]
    for i in range(1, len(A)):
        f.append(max(A[i],f[i-1]))
    return f


def submax(f, last):
    print(f[last])


f = totalmax(A)
q=4
submax(f, q)
