a=[1,2,4,5,5,5,6,8,9]
k=3


def check(a,k):
    first=0
    last=len(a)-1
    out = -1
    while first<=last:
        mid=(first+last)//2
        if(a[mid]==k):
            out = mid
            last=mid-1

        elif(a[mid]>k):
            last=mid-1

        else:
            first=mid+1
    
    print(out)

check(a,5)