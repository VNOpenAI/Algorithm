


def quicksort(a,first,last):
    i=first
    j=last
    k=a[(i+j)//2]
    while i < j :
        while a[i] < k : i+=1
        while a[j] > k : j-=1
        if(i<=j):
            a[i],a[j]=a[j],a[i]
            i+=1
            j-=1

    if(i<last) :  quicksort(a,i,last)   # i với cuối 
    if(j>first) :  quicksort(a,first,j) # đầu với j
   

a=[5,3,2,1,5,6,7]
quicksort(a,0,len(a)-1)
print(a)

# cần cm :
    # nếu i<j = > dãy a1[first:i] dãy a2[j:last]  chỉ cần sắp xếp a1 và a2 => a=a1+a2[]