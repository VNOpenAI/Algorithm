 #input a đã sắp tăng 
 # số k
 #output k in a ?
import time

# a=list(range(0,1000000,2))
# k=50000


# t1=time.time()

# print(k in a)

# print(time.time()-t1)


def check(a,k):
    first=0
    last=len(a)-1
    while first<=last:
        mid=(first+last)//2
        if(a[mid]==k):
            return 1
        if(a[mid]>k):
            last=mid-1
        else:
            first=mid+1
    
    return -1

t1=time.time()
print(check(a,k))
print(time.time()-t1)





# def swap(a,b):
#     tmp=a
#     a=b
#     b=tmp
# def change(a):
#     a[0]=2

# x=1
# y=2
# swap(x,y)
# print(x)
# print(y)    

# change(a)
# print(a)
