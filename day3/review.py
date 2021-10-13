'''
Bài toán đệ quy Recursion:
    Bước 1: Định nghĩa chức năng hàm
    Bước 2: Định nghĩa neo, điểm dừng (nếu không thì sẽ giống như while ko dừng)
    Bước 3: Xác định bài toán con và mối liên hệ với bài toán cha
'''
'''B1: uoc chung lớn nhất
UCLN(a, b) = UCLN(b, a mod b) ....=> a mod b = 0 => return a'''
def UCLN(a, b):
    if b == 0:
        print(a)
    else:
        UCLN(b, a % b)

UCLN(4,30)

'''
tim kiem nhi phan
kiem tra k co nam trong a hay khong
DInh nghia BS(a,f,l,k) : tim kiem k trong doan tu f->l cua a
'''

def BS(a, f, l, k):
    mid = (f+l)//2
    if f > l:
        print("Not found!")
        return 0

    if k >a[mid]: 
        BS(a, mid+1, l, k)
    elif k < a[mid]:
        BS(a, f, mid - 1, k)
    elif k == a[mid]:
        print("Found at position: %s" %mid)

'''
So fibonaci
'''

def fibonaci(n):
    if n <= 1:
        return 1
    else:
        return fibonaci(n-1)+fibonaci(n-2)
n = 4
print("Fibonaci of %s: %s" %(n, fibonaci(n)))

'''
Bài toán Vét cạn (Quay lui) Backtracking:
chia làm 2 loại:
    1 : cố định đầu ra của output
    2 : không cố định đầu ra
'''

##a) sinh ra số có k chữ số từ 1->M (các số có thể trùng nhau ví dụ k=3,m=5 =>111,123 )
m = 5
k = 3

s = [0]*k
def output():
    print(*s, sep='')
def B(i):
    for j in range(1,m+1):
        s[i] = j
        if i == k-1:
            output()
        else:
            B(i+1)

B(0)
    

# # b) sinh ra số có k chữ số từ 0->M (các số có thể trùng nhau ví dụ k=3,m=5 =>100)   
# #     thêm điều kiện if((i==0 and j!=0) or i!=0)
# #     xét a[0]:1->M gọi backtracking từ i=1
k = 3
m=5
s = [0]*k

def output():
    print(*s, sep='')

def B(i):
    for j in range(m+1):
        if (i == 0 and j>0) or (i>0):
            s[i] = j
            if i == k-1:
                output()
            else:
                B(i+1)
B(0)

# #c) sinh ra số có số chữ số nhỏ hơn M từ các chữ số từ 1->M (các số cỏ thể trùng nhau):
#     # cứ đẩy j vào thì gọi output
m = 4
s= [0]*(m-1)
def output(i):
    print(*s[:i+1], sep='')
def B(i):
    for j in range(1,m+1):
        s[i] = j
        if i == m-2:
            output(i)
        else:
            output(i)
            B(i+1)

B(0)



#d) sinh ra số có k chữ số từ 1->M (các số không  thể trùng nhau ví dụ k=3,m=5 =>123)
    # cần mảng đánh dấu chú ý trả đánh dấu khi mà không khi không lấy phần tử đấy nữa

k = 3
m = 5
c = {}
s = [0]*k
def output():
    print(*s, sep='')
def B(i):
    for j in range(1,m+1):
        if j not in c:
            s[i] = j
            c[j] = 0
            if i == k-1:
                output()
            else:
                B(i+1)
            del c[j]
B(0)

#e) sinh ra số có k chữ số từ 1->M (chữ số sau lớn hơn chữ số trước)
    # kiểm tra trùng ( đánh dấu ) + kiểm tra j>a[i-1] 
k = 3
m = 5
c = {}
s = [0]*(k+1)
def output():
    print(*s[1:], sep='')
def B(i):
    for j in range(1,m+1):
        if j not in c and j>s[i-1]:
            s[i] = j
            c[j] = 0
            if i == k:
                output()
            else:
                B(i+1)
            del c[j]
B(1)  