# dãy con tăng dài nhất 
# 1 3 2 4 6 1 =>  res_arr=1 2 4 6  # theo value
                # res_indexs 0 2 3 4 
                # cần xây dựng mảng trace
                # trace[i]=j nếu trong dãy kết quả thì trước cái a[i] sẽ là a[j]

# trace[0]=-1
# trace[1]=0
# trace[2]=0
# trace[3]=2
# trace[4]=3
# trace[5]=-1

# f[4]=4(max f) ->res_id=4 
# 4->3 ->2->0

a=[1,3,2,4,6,1]

f=[1]#f[0]=1
res=f[0]

# trace[4]=3 (a[3]=4,a[4]=6) 
trace=[-1] # trace[0]=-1 


for i in range(1,len(a)):
    f.append(1) # f[i]=1
    trace.append(-1)
    for j in range(i-1,-1,-1):
        if(a[j]<a[i]):
            # f[i]=max(f[i],f[j]+1)
            if(f[j]+1>f[i]):
                f[i]=f[j]+1
                trace[i]=j
    
    # res=max(res,f[i])
    if(res<f[i]):
        res_id=i
        res=f[i]

print(res," and index = ",res_id)
id=res_id
res_arr=[]
while id!=-1:
    # print(a[id],end=" ")
    res_arr.append(a[id])
    id=trace[id]

print(res_arr[::-1])
