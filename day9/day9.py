'''
Bài 1:
tìm dãy con(liên tục) có tổng lớn nhất
vd a=[1,2,-4,3,-1,2]
    output : 3 - 1 2

f[i] là tổng lớn nhất của các dãy con kết thúc tại i 
f[i]= max(f[i-1]+a[i],a[i])
f[0]=a[0]
kết quả max(f)
'''
a=[1,2,-4,3,-1,2]
# Solution 1: Backtrack
max_s = 0
max_i = 0
max_j = 0
for i in range(len(a)):
    for j in range(i, len(a)):
        s = sum(a[i:j+1])
        if s>max_s:
            max_s = s
            max_i, max_j = i, j

print(max_s,'\n', max_i, '\n', max_j)


# solution 2: Dynamic Program

f=[a[0]]
res=f[0]
for i in range(1,len(a)):
    f.append(max(f[i-1]+a[i],a[i]))
    if(f[i]>res):
        res=f[i]
        last = i

print(res)
s=0
for i in range(last,-1,-1):
    s+=a[i]
    if(s==res):
        first=i
        break
print('a[',first,'->',last,"] = ",res)