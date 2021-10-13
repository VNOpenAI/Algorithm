'''
1.	Cho dãy số nguyên bất kì : hỏi k có trong dãy số hay không
'''

import sys
sys.path.append(
    r'D:\OneDrive - Hanoi University of Science and Technology\Intern\Training\DA')

from day1.sort import CustomSort

def check_unsort(a, k):
    for i in a:
        if k == i:
            return 1
        else:
            return -1


arr = [5, 110, 25, 11, 13]
k = 7
print("Ex1: %s" % check_unsort(arr, k))

'''
2. Cho dãy A sắp xếp tăng dần , kiểm tra X có nằm trong dãy hay không
'''


def check_sort(a, k):
    first = 0
    last = len(a)-1
    while first <= last:
        mid = (first+last)//2
        if(a[mid] == k):
            return 1
        if(a[mid] > k):
            last = mid-1
        else:
            first = mid+1
    return -1


arr2 = [5, 5, 6, 11, 13]
k2 = 7
print("Ex2: %s" % check_sort(arr, k))

'''
3. Nâng cao : Có N cây gỗ, có chiều cao lần lượt là A[1],A[2],..,A[n]. 
Bạn cần lấy một lượng gỗ độ cao tối thiểu là M bằng cách chặt từ N cây theo cách như sau: 
chặt tất cả những phần thừa của các cây có độ cao lớn hơn H. 
Hãy tìm giá trị H lớn nhất để bạn có thể lấy được lượng gỗ tối thiểu là M

# Brainstorm:
input: 
    a0....an
    M
output: 
    H

condition: Sum (ai+..+an - (n-i+1)*H) = M, với ai>H
=> Thuật toán có xu hướng giảm: vì H càng nhỏ thì càng thỏa mãn điều kiện
                                    H0 => thỏa mãn => H0-k => Thỏa mãn
    output: Min = 0, Max = max(a)
    Solution: Tìm H trong list(Min, Max) thỏa mãn điều kiện => Binary_search

'''


def check(mid, M, a):
    '''return Bool value. True if s>=M'''
    s = 0
    for x in a:
        if x > mid:
            s += (x-mid)
    if (s >= M):
        return True

    return False


def find_res(arr, M):
    sort = CustomSort(arr)
    sort.merge_sort(arr)
    Min = 0
    Max = arr[-1]
    a = [*range(Min, Max, 1)] # create output array from Min to Max
    while Min <= Max:
        mid = (Min+Max)//2
        if check(mid, M, a):
            res = mid
            Min = mid+1 # if mid meet condition, increase mid until it cannot meet condition
        else:
            Max = mid-1 # if mid not meet condition, decrease mid until it cannot meet condition
    return res


arr = [78, 92, 15, 48, 64, 30]
m = 4
print("Ex3: %s" % find_res(arr, m))
