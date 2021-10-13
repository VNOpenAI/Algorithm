# def merge_sort(self,arr):#5/10
#         if len(arr) > 1:
#             mid = len(arr)//2
#             a1 = arr[:mid]
#             a2 = arr[mid:]
#             sort1 = self.merge_sort(a1)
#             sort2 = self.merge_sort(a2)


#             # a1_idx, a2_idx: idx in 2 self.arr. respectively. sorted_idx: idx in sorted self.arr.
#             a1_idx, a2_idx, sorted_idx = 0, 0, 0
#             # compare ele in 2 self.arr and add the
#             while (a1_idx < len(a1)) and (a2_idx < len(a2)):
#                 if a1[a1_idx] <= a2[a2_idx]:
#                     self.arr[sorted_idx] = a1[a1_idx]
#                     a1_idx += 1
#                 else:
#                     self.arr[sorted_idx] = a2[a2_idx]
#                     a2_idx += 1
#                 sorted_idx += 1
#             if a1_idx < len(a1):
#                 self.arr[sorted_idx:] = a1[a1_idx:]
#             if a2_idx < len(a2):
#                 self.arr[sorted_idx:] = a2[a2_idx:]

# Review
arr = [11,4,23,54,11,23,2]
def insertionSort(a):
    for i in range(1,len(a)):
        cur_val = a[i]
        cur_idx = i
    
        while cur_idx > 0 and cur_val < a[cur_idx-1]:
            a[cur_idx] = a[cur_idx-1]
            cur_idx -=1
        a[cur_idx] = cur_val
    return a

print(insertionSort(arr))

arr = [11,4,23,54,11,23,2]
def selectionSort(a):
    for i in range(len(a)-1):
        min_idx = i
        for j in range(i+1,len(a)):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a
print(selectionSort(arr))

arr = [11,4,23,54,11,23,2]
def bubbleSort(a):
    for i in range(len(a)-1):
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a
print(bubbleSort(arr))

arr = [11,4,23,54,11,23,2]
def countingSort(a):
    max_val = a[0]
    for i in a:
        if i > max_val:
            max_val = i

    c = [0] * (max_val+1)

    for i in a:
        c[i] += 1
    idx = 0
    for j in range(max_val+1):
        for i in range(c[j]):
            a[idx] = j
            idx += 1    
    return a
print(countingSort(arr))

arr = [11,4,23,54,11,23,2]
def mergeSort(a):
    if len(a) > 1:
        mid = len(a)//2
        a1 = a[:mid]
        a2 = a[mid:]
        mergeSort(a1)
        mergeSort(a2)

        idx1, idx2, sorted_idx = 0, 0, 0
        while idx1< len(a1) and idx2 < len(a2):
            if a1[idx1] <= a2[idx2]:
                a[sorted_idx] = a1[idx1]
                idx1+=1
            else:
                a[sorted_idx] = a2[idx2]
                idx2+=1
            sorted_idx+=1
        if idx1 < len(a1):
            a[sorted_idx:] = a1[idx1:]
        else:
            a[sorted_idx:] = a2[idx2:]

mergeSort(arr)
print(arr) 

arr = [11,4,23,54,11,23,2]
def quickSort(a, first, last):
    i = first
    j = last
    k = a[(i+j)//2]

    while a[i] < k: 
        i+=1
    while a[j] > k:
        j-=1
    if i <= j:
        a[i], a[j] = a[j], a[i]
        i+= 1
        j-=1
    if i<last: quickSort(a, i, last)
    if j>first: quickSort(a,first, j)
quickSort(arr, 0, len(arr)-1)
print(arr)






    