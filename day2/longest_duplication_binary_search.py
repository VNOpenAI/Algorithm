'''
BÀI TOÁN: Tìm 2 dãy con trùng nhau từ 1 dãy:

    quy về bài toán kiểm tra có tồn tại ít nhất 2 dãy con có độ dài l giống nhau không

  ->   ham check (a,l) -> return [start_of_arr2, start_of_arr1, l] if arr2 == arr1
  -> how to choose l?
    - l is from min to max 
            min = 0
            max = n//2
 -> if found l, increase l => check(a,l)
    else: decrease l => check(a,l)


    check(a,l):
        for i in range(len(a)):
            s = n_elements of a
            dictSearch c: c[s] = start of s
            if s in c and i-dict[s] >= l:
                return out
        not found => return [-1, -1, -1]
    ptu neo: s, c (can khoi tao)

    # example: 
    # tai vi tri i thi minh xet xau s[i:l+i] 
    # tại vị trí i có xâu si ( chính là s[i:l+i]) cần lưu vị trí đầu tiên của si
    # ví dụ
    # l=3 ab b c a b c d
        # s0 ab b c 0
        # s1 b c a 1
        # s2 c a b 2
        # s3 a b c i=3 -dict[abc](0)>=3 
        # s4 b c d 4

    # l=2
        #bbbb
        #s0 bb dict[bb]=0
        #s1 bb 
        #s2 bb  #i - dict[x]>=l thoa man
'''
a=["a","b","c","b","c","a","b","c","b"]
n=len(a)

def check(a,l):

    n=len(a)
    c={} # dict để lưu vị trí của xâu xuất hiện đầu tiên
    #init
    s=""
    for i in range(0,l):
        s+=a[i]+" "
    len_pre=len(a[0]) # deal with cases: when length of each element is fixed
    s=s[:-1]
    c[s]=0
   
    #end init

    for i in range(1,n-l+1): # i 
        s=s[len_pre+1:]+" "+a[i+l-1] # bỏ element đầu tiên đi, thêm vào element mới
       # i=3 -dict[abc](0)>=l
        find =c.get(s,-1)
        if(find!=-1):
            if(i-c[s]>=l):
                return [find,i,l]
        else:
            c[s]=i
    return [-1,-1,-1]

                




first = 0
last = n//2
res=[-1,-1,-1]
while first<=last:
    mid=(first+last)//2
    [f1,f2,l] = check(a,mid)
    if(f1!=-1):
        res=[f1,f2,l]
        first = mid+1
    else:
        last = mid -1
print(res)




