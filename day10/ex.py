'''
1. Tìm dãy con (liên tiếp) tăng, giảm, không giảm, không tăng dài nhất.
'''
# tăng
a = [1, 3, 2, 2, 1, 4, 6, 6, 1]


def increase(a):
    f = [1]  # f[0] = 1
    MAX = 1
    end = 0
    for i in range(1, len(a)):
        if a[i] > a[i-1]:
            f.append(f[i-1]+1)
            if f[i] > MAX:
                MAX = f[i]
                end = i
        else:
            f.append(1)
    print("Day lien tiep tang dai nhat: %s -> %s" % (end+1-MAX, end))


increase(a)

# giảm


def decrease(a):
    f = [1]  # f[0] = 1
    MAX = 1
    end = 0
    for i in range(1, len(a)):
        if a[i] < a[i-1]:
            f.append(f[i-1]+1)
            if f[i] > MAX:
                MAX = f[i]
                end = i
        else:
            f.append(1)
    print("Day lien tiep giam dai nhat: %s -> %s" % (end+1-MAX, end))


decrease(a)

# không giảm


def n_decrease(a):
    f = [1]  # f[0] = 1
    MAX = 1
    end = 0
    for i in range(1, len(a)):
        if a[i] >= a[i-1]:
            f.append(f[i-1]+1)
            if f[i] > MAX:
                MAX = f[i]
                end = i
        else:
            f.append(1)
    print("Day lien tiep khong giam dai nhat: %s -> %s" % (end+1-MAX, end))


n_decrease(a)

# không tăng


def n_increase(a):
    f = [1]  # f[0] = 1
    MAX = 1
    end = 0
    for i in range(1, len(a)):
        if a[i] <= a[i-1]:
            f.append(f[i-1]+1)
            if f[i] > MAX:
                MAX = f[i]
                end = i
        else:
            f.append(1)
    print("Day lien tiep khong tang dai nhat: %s -> %s" % (end+1-MAX, end))


n_increase(a)

'''
Bai 2: Dãy con (bất kì ) tăng dài nhất: 
'''
a = [1,0,1,2,3,2,4]
def increase2(a):
    f = [1]  # f[0] = 1
    trace=[-1] # trace[0]=-1 
    MAX = 1
    for i in range(1, len(a)):
        f.append(1) # f[i] = 1
        trace.append(-1)
        for j in range(i-1,-1,-1):
            if a[j] < a[i]:
                if f[j]+1>f[i]:
                    f[i] = f[j]+1
                    trace[i] = j
        if f[i] > MAX:
            MAX = f[i]
            end = i
    out = []
    while end !=-1:
        out.append(a[end])
        end = trace[end]
    print(out[::-1])

increase2(a)

'''Bài 3: tìm dãy B(liên tiếp) trong dãy A(liên tiếp):
'''
A = [2,3,1,2,3,4,5,12]*5
B = [2,3,4]

import time
## break after found
# def subarr(A, B):
#     f = []
#     n, k = len(A), len(B)
#     base = {"_".join([str(x) for x in B]):1}
#     for i in range(n-k+1):
#         t = 0
#         tmp = ""
#         while t < k:
#             tmp += str(A[i+t])+'_'
#             t+=1
#         f.append(tmp[:-1])
#         if f[i] in base:
#             print("Found: %s -> %s" %(i, i+k-1))
    
# start = time.time()
# subarr(A, B)
# print("Take time: %s" %(time.time()-start))


def subarr(A, B):
    f = []
    n, k = len(A), len(B)
    base = "_".join([str(x) for x in B])
    for i in range(n-k+1):
        t = 0
        tmp = ""
        while t < k:
            tmp += str(A[i+t])+'_'
            t+=1
        f.append(tmp[:-1])
    for j in range(10):
        start = time.time()
        for i in range(n-k+1):
            if f[i] == base:
                print("Found: %s -> %s" %(i, i+k-1))
        print("Take time (==): %s" %(time.time()-start))
    

subarr(A, B)


def subarr(A, B):
    f = []
    n, k = len(A), len(B)
    base = {"_".join([str(x) for x in B]):1}
    for i in range(n-k+1):
        t = 0
        tmp = ""
        while t < k:
            tmp += str(A[i+t])+'_'
            t+=1
        f.append(tmp[:-1])
    start = time.time()
    for i in range(n-k+1):
        if f[i] in base:
            print("Found: %s -> %s" %(i, i+k-1))
    print("Take time (dict): %s" %(time.time()-start))
    

subarr(A, B)
