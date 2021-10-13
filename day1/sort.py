class CustomSort:
    def __init__(self, arr):
        self.arr = arr

    def insertion_sort(self):
        # Start from 1 since the 1st ele is trivially sorted
        for i in range(1, len(self.arr)):

            curr_val = self.arr[i]
            curr_idx = i

            # As long as we haven't reached the beginning and there is an element
            # in our sorted self.array larger than the one we're trying to insert - move
            # that element to the right

            while curr_idx > 0 and curr_val < self.arr[curr_idx-1]:
                self.arr[curr_idx] = self.arr[curr_idx-1]
                curr_idx -= 1
            self.arr[curr_idx] = curr_val

    def selection_sort(self):
        # i indicates how many items were sorted
        for i in range(len(self.arr)-1):
            # assume the min val is the 1st ele
            min_idx = i

            # Find the min in self.arr[i+1,end] then swap
            for j in range(i+1, len(self.arr)):
                if self.arr[j] < self.arr[min_idx]:
                    min_idx = j
            self.arr[i], self.arr[min_idx] = self.arr[min_idx], self.arr[i]

    def bubble_sort(self):
        # repeat n-1 iter
        for i in range(len(self.arr)-1):

            # swap until the max ele is in the last pos
            for j in range(len(self.arr)-1):
                if self.arr[j] > self.arr[j+1]:
                    self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]

    def counting_sort(self):
        # initial bucket to store couting val
        max_val = 0
        for i in range(len(self.arr)):
            if self.arr[i] > max_val:
                max_val = self.arr[i]

        bucket = [0] * (max_val+1)

        # store counting to bucket
        for j in self.arr:
            bucket[j] += 1

        # place ele ith due to counting val
        idx = 0
        for j in range(max_val+1):
            for i in range(bucket[j]):
                self.arr[idx] = j
                idx += 1

    def merge_sort(self, arr):
        if len(arr) > 1:
            mid = len(arr)//2
            a1 = arr[:mid]
            a2 = arr[mid:]
            self.merge_sort(a1)
            self.merge_sort(a2)

            # a1_idx, a2_idx: idx in 2 arr. respectively. sorted_idx: idx in sorted arr.
            a1_idx, a2_idx, sorted_idx = 0, 0, 0
            # compare ele in 2 self.arr and add the
            while (a1_idx < len(a1)) and (a2_idx < len(a2)):
                if a1[a1_idx] <= a2[a2_idx]:
                    arr[sorted_idx] = a1[a1_idx]
                    a1_idx += 1
                else:
                    arr[sorted_idx] = a2[a2_idx]
                    a2_idx += 1
                sorted_idx += 1
            if a1_idx < len(a1):
                arr[sorted_idx:] = a1[a1_idx:]
            if a2_idx < len(a2):
                arr[sorted_idx:] = a2[a2_idx:]
    
    def quick_sort(self):
        pass

if __name__ == "__main__":
    arr = [11,4,23,54,11,23,2]
    sort = CustomSort(arr)
    sort.merge_sort(arr)
    print("Sorted self.array is:", arr)

