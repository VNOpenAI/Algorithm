
'''
ví dụ 1  có 1 dãy A[1,6,3,2,5]
kiểm tra xem có k số để tổng M = 9
'''
k = 3
arr = [1, 6, 3, 2, 5, 2, 3, 5]
M = 9
# c = {}

n = len(arr)
a = k*[0]
check = False


def output():
    global check
    s = 0
    for x in a:
        s += x
    if s == M:
        check = True
        print(check)
    return check


def P(i):
    global check
    for j in range(i, n):
        if not check:
        # if (arr[j] not in c) and not check:
            a[i] = arr[j]
            # c[arr[j]] = 0
            if i == k-1:
                output()
            else:
                P(i+1)
            # del c[arr[j]]


P(0)
#     '''
#     # bài toán
#     #     input n
#     #     output số có n chữ số lập từ 1->n
#     #     n=3
#     #     111
#     #     112
#     #     ...
#     '''
#     n = 3
#     a = [0]*n


#     def output():
#         for i in range(n):
#             print(a[i], end=' ')
#         print()


#     def P(i):  # find a[i->n-1] value from j(1,n+1)
#         for j in range(1, n+1):
#             a[i] = j  # input j in a[i]
#             if i == n-1:
#                 output()
#             else:
#                 P(i+1)


#     P(0)

#     # # -> O(n^n)
#     '''
#     ví dụ
#         n=3
#         P(0): cần điền từ a[0]->a[n]
#         a[0] : nhận lần lượt các giá trị của j
#         a[0] = 0
#         i=0!=2
#         => gọi P(1):
#         j=0 =>a[1]=0
#         i=1!=2
#         gọi P(2)
#         a[2]=0 

#         i=2==2 => output( dãy a)
#         j=1 => a[2]=1 => output(dãy a)
#         j=2 =>.....

#         sinh ra số có k chữ số từ [1->n]
#         ví dụ n=5,k=3
#         111,112,113,114,115
#     '''
#     n = 5
#     k = 3
#     a = [0]*k


#     def output():
#         for i in range(k):
#             print(a[i], end=" ")
#         print()


#     def P(i):  # P(i) là điền kết quả vào dãy a từ a[i->n-1]
#         for j in range(1, n+1):  # j là các kết quả có thể thêm vào a[i]
#             a[i] = j
#             if(i == k-1):
#                 output()
#             else:
#                 P(i+1)


#     P(0)
#     # dpt => O(k^n)

#     '''
#     ví dụ 3:
#         input n
#         output số có k chữ số lập từ 1->n(trong mỗi số chữ số không được giống nhau)
#         n=5
#         123
#         124
#         ...
#     '''
#     n = 5
#     k = 3
#     a = [0]*k
#     c = {}


#     def output():
#         for i in range(k):
#             print(a[i], end=' ')
#         print()


#     def P(i):  # P(i) là điền kết quả vào dãy a từ a[i->n-1]
#         for j in range(1, n+1):  # j là các kết quả có thể thêm vào a[i]
#             if(j not in c):
#                 a[i] = j
#                 c[j] = 0
#                 if(i == k-1):
#                     output()

#                 else:
#                     P(i+1)

#                 del c[j]


#     P(0)

# '''
# ví dụ 4:
# tim k số có tổng bằng M từ dãy arr
# in kết quả không trùng nhau
# <=> in kết quả theo thứ tự tăng dần
# '''
# ##### chua nghi ra#######
# k = 4
# arr = [1, 6, 3, 2, 5, 2, 3, 5]
# M = 9
# c = {}
# a = (k+1)*[0]
# a[-1]=-1
# s=0

# # res :  a=[0 1 3]
# n=len(arr)
# check=False

# def P(i):
#     global s
#     for j in range(0,len(arr)):
#         if (j not in c) and (s+arr[j]<=M) and (j>a[i-1]) :

#             a[i] = j
#             c[j] = 0
#             s+=arr[j]

#             if i==k-1:
#                 if s==M:
#                     for id in a[:-1]:
#                         print(arr[id],end=" ")
#                         check=True
#                     print()   
#             else:
#                 P(i+1)

#             s-=arr[j]
#             del c[j]

# P(0)



# '''
# ví dụ 5:
# tim k số có tổng bằng M từ dãy arr
# in kết quả không trùng nhau
# <=> in kết quả theo thứ tự tăng dần
# '''

# k = 4
# arr = [1, 6, 3, 2, 5, 2, 3, 5]
# M = 9
# c = {}
# a = (k+1)*[0]
# a[-1]=-1
# s=0

# # res :  a=[0 1 3]
# n=len(arr)
# check=False
# check_res={}


# #1 2 2 3
# #1 3 2 2
# #1 2 2 3

# def P(i):
#     global s
#     for j in range(0,len(arr)):
#         if (j not in c) and (s+arr[j]<=M) and (j>a[i-1]) :

#             a[i] = j
#             c[j] = 0
#             s+=arr[j]

#             if i==k-1:
                
#                 if s==M :
#                     res_str=""
#                     for id in a[:-1]:  
#                         res_str+=str(arr[id])+"_"

#                     if(res_str not in check_res):
#                         for id in a[:-1]:
#                             print(arr[id],end=" ")
#                         print() 

#                     check_res[res_str]=0

#             else:
#                 P(i+1)

#             s-=arr[j]
#             del c[j]

# P(0)