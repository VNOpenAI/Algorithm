# kiểm tra tồn tại k số trong arr sao cho bằng M
k = 3
arr = [1,6,3,2,5,2,3,5]
M = 9
c = {}

n=len(arr)
a=len(arr)*[0]
check=False

def output():
    # print(a)
    s=0
    for x in a:
        s+=a
    if(s==M):
       print(a)


# def P(i):#P(i) là điền kết quả vào dãy a từ a[i->n-1] 

#         for j in range(0,n): # j là các kết quả có thể thêm vào a[i]
#             if(j not in c and  j>a[i-1]):
#                 a[i]=j
#                 c[j]=0
#                 if(i==k-1):
#                    output()
#                 else: 
#                     P(i+1)
                    
#                 del c[j]#?????????????????????????????????
    
# for j in range(0,n-k):
#     a[0]=j
#     P(0)

# nhánh cận
    s=0 # tổng từ 0 đến i
    def P(i):#P(i) là điền kết quả vào dãy a từ a[i->n-1] 

            for j in range(0,n): # j là các kết quả có thể thêm vào a[i]
                if(j not in c and  j>a[i-1] and s+j<=M):
                    a[i]=j
                    c[j]=0
                    s=s+j

                    # if(i==k-1):
                    #     output()
                    if(s==M):
                        output()
                    else: 
                        P(i+1)

                    s-=j    
                    del c[j]#?????????????????????????????????
        
    for j in range(0,n-k):
        a[0]=j
        if(j<M):
            s=j
            P(0)

print(check)


#
    dãy a[0...n-1]
    H sao tổng(a[i]-H)>=M( với a[i]>H)

    # nhận xét 
            # H0 => thỏa mãn => H0-k => Thỏa mãn
            # kqua Min , Max  , Min=0, Max=10000000
    Max =max(a)

    res=-1

    def check(H):
        s=0
        for x in a:
            if(x>H):
                s+=(x-H)
        if(s>=M):
            return True
        return False 


    def find_res(Min,Max):
        mid = (Min+Max)//2
        if(check(mid)):
            res=mid
            Min=mid+1
        else:
            Max=mid-1
