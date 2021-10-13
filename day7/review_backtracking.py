'''
Bài tập 1
n=6
A=[1,2,2,5,10,10]
# chia item cho 2 phần sao cho tổng 2 phần bằng nhau
    # Chị Thủy Xinh gái : 1 2 2 10
    # Em Hảo đẹp trai : 5 10
    # A 0 1 2 4
    # B 3 5 
'''
A = [1, 2, 2, 5, 10, 10]

# Chị Thủy Xinh Gái
# Nâng chị như nâng kim cương
def backtrack(i, A, half):
    global s, a, check_res
    for j in range(a[i-1]+1,len(A)):
        if (s + A[j] <= half):
            a[i] = j
            s += A[j]
            if s == half:
                res_str = ""
                for j in a[:i+1]:
                    res_str+=str(A[j])+' '
                if res_str not in check_res:
                    check_res[res_str] = 0
                else:
                    for j in a[:i+1]:
                        print(A[j],end=" ")
                    print() 
            elif s < half:
                backtrack(i+1, A, half)
            s -= A[j]


def split_half(A: list):
    global s, a, check_res
    check_res = {}
    a = [0]*(len(A)+1)
    a[-1] = -1
    s0, s = 0, 0
    for x in A:
        s0 += x
    if (s0 % 2 != 0) or (max(A) > s0/2):
        print("can't split!!!!")
    else:
        half = s0/2
        backtrack(0, A, half)


split_half(A)

'''
bài 2:
có 1 cái túi chỉ đựng được M(kg)
  CHị Thủy có n đồ vật (mỗi đồ vật có khối lượng m_i, giá trị val_i)
  Tìm cách chọn một số đồ vật sao cho giá trị lớn nhất và khối luợng <=M

    gợi ý 1 hướng giải khác: sắp xếp theo val_i/m_i ( xem những thằng ở đầu mang giá trị cao hơn thằng sau)
'''

weight = [1,  2  , 4 , 4,  6,  9]
value =  [1,  7  , 8 , 8,  11, 15]

M = 10

a = [0]*(len(value)+1)

a[-1] = -1
v = 0
max_v = 0
w = 0
res = []

def P(i):
    global v,w, max_v, res

    for j in range(a[i-1]+1,len(value)):
        if (w+weight[j]<=M):
            a[i] = j
            w+=weight[j]
            v += value[j]
            if v>max_v:
                max_v = v
                res = a[:i+1].copy() # nếu v = max_v thì sao?
            P(i+1)
           
            v-=value[j]
            w-=weight[j]
P(0)
        
print(res)




