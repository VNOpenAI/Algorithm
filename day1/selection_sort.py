 
a=[1,2,5,4,-3]
n=len(a)
for i in range(0,n-2):
    # tim phan tu nho nhat tu i-j
    min_value = a[i]
    min_index = i
    for j in range(i+1,n):
        if ( a[j]<min_value):
            min_index=j
            min_value=a[j]
        

