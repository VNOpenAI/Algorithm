def normSearch(a, k):
    found = 0
    for i in range(len(a)):
        if a[i] == k:
            print("Found at position: %s" % i)
            found = 1
    if not found:
        print("Not found!")


arr = [2, 5, 6, 2, 5, 4]
normSearch(arr, 2)


def dictSearch(a, k):
    c = {}
    for i in range(len(a)):
        if a[i] in c:
            c[a[i]].append(i)
        else:
            c[a[i]] = [i]
    if k in c:
        print("Found at position: %s" % c[k])
    else:
        print("Not found!")


arr = [2, 5, 6, 2, 5, 4]
dictSearch(arr, 2)


def binarySearch(a, k):
    '''require a is sorted'''
    found = 0
    first = 0
    last = len(a)-1

    while first < last and not found:
        mid = (first+last)//2
        if k == a[mid]:
            print("Found at position: %s" % mid)
            found = 1
        elif k < a[mid]:
            last = mid - 1
        else:
            first = mid + 1

    if not found:
        print("Not found!")
    else:
        for i in range(mid-1, -1, -1):
            if a[i] == k:
                print("Found at position: %s" % i)
            else:
                break
        for i in range(mid+1, len(a)):
            if a[i] == k:
                print("Found at position: %s" % i)
            else:
                break


sorted_arr = [2, 2, 4, 5, 6, 7, 8]
binarySearch(sorted_arr, 2)


a = ["a", "b", "c", "b", "c", "a", "b", "c", "b"]


def check(arr, l):
    c = {}
    for i in range(len(a)-l+1):
        s = '_'.join(a[i:i+l])
        if s not in c:
            c[s] = i
        else:
            if i-c[s]>= l:
                return [l, i, c[s]]
    return [-1,-1,-1]
check(a,5)
def longest_dup_search(arr):
    MIN = 0
    MAX = len(arr)//2
    found = 0
    while MIN <= MAX:
        MID = (MIN+MAX)//2
        tmp = check(arr, MID)
        if tmp[0] != -1:
            MIN = MID+1
            res = tmp
            found = 1
        else:
            MAX -= 1
    if not found:
        print("Not found any duplicates!")
    else:
        print("Found duplicate from %s -> %s and %s -> %s having lenghth: %s" %
              (res[2], res[2]+res[0], res[1], res[1]+res[0], res[0]))

longest_dup_search(a)