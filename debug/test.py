#Breakpoints : đó là điểm dừng 
#step over : di chuyển xuống dòng tiếp theo
#step into : di chuyển đến lệnh tiếp theo
#step out  : nhảy đến breakpoints tiếp theo
# watch : xem biến , hàm 



def sum(a):
    s=0
    for x in a:
        s+=x
    return a

def add(a,k):
    for x in a:
        x+=k



a=0
a+=1
b=a+1


c=[1,2,3,5]
c[0]=c[0]+a

s=sum(c)

add(c,3)


a+=1