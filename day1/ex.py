'''
1. Cho danh sách học sinh lớp A  biết chiều cao và cân nặng của n bạn học sinh, 
sắp xếp danh sách học sinh theo thứ tự tăng dần chiều cao, 
trong trường hợp chiều cao bằng nhau thì sắp  xếp theo cân nặng
'''

from sort import CustomSort
import numpy as np


def sort_height_weight(arr):
    # repeat n-1 iter
    for i in range(len(arr)-1):

        # swap until the max ele is in the last pos
        for j in range(len(arr)-1):
            if arr[j][0] > arr[j+1][0]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            elif (arr[j][0] == arr[j+1][0]) & (arr[j][1] > arr[j+1][1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]


# Test
arr = [(158, 40), (180, 70), (150, 40), (149, 36), (158, 39)]
sort_height_weight(arr)
print("Ex1: %s" % arr)


'''
2. Cho mảng N phần tử (N rất lớn , mỗi phần tử nằm trong khoảng [0,10^8]
sắp xếp mảng N tăng dần
'''

arr1 = list(np.random.randint(0, 10**8, 5))
res = CustomSort(arr1)
res.counting_sort()
print("Ex2: %s" % arr1)


'''
3. Cho dữ liệu vào là luồng stream gồm các phần tử là số , 
tại thời điểm bất kì cần xuất ra dãy hiện tại được sắp xếp tăng dần
'''
old_arr = [5, 5, 6, 11, 13]
add_arr = [7, 5, 6]


def binary_search(a, k):
    if k < a[0]:
        return 0
    elif k > a[-1]:
        return len(a)
    else:
        first = 0
        last = len(a)-1
        while first <= last:
            mid = (first+last)//2
            if(a[mid] == k):
                return mid
            if(a[mid] > k):
                last = mid-1
            else:
                first = mid+1
        return mid

# # Test
# assert binary_search(old_arr,17) == 5, "error"


def insertion_sort_after_add(old_arr, add_arr):
    # Start from 1 since the 1st ele is trivially sorted
    old_arr += add_arr
    a = 0
    for i in range(len(old_arr)-len(add_arr), len(old_arr)):
        idx = binary_search(old_arr[:len(old_arr)-len(add_arr)+a], old_arr[i])
        if idx < len(old_arr) - 1:
            old_arr[idx+1:] = old_arr[idx:-1]
        else:
            old_arr[idx], old_arr[i] = old_arr[i], old_arr[idx]
        a += 1


insertion_sort_after_add(old_arr, add_arr)
print("Ex3: %s" % old_arr)
