# quicksort :
    # DỰA VÀO ĐỆ QUI
    # Tìm 1 vị trí của dãy , kết hợp với swap sao cho tại vị trí đó(index) phần bên trái sẽ nhỏ hơn arr[index] phần bên phải nó sẽ lớn hơn arr[index]
    # 4 3 2 5 8 7 6
    # vị trí arr[3]=5 
    # Trung bình độ phức tạp là O(NLogN) 
# tìm 1 số để làm khóa :
    # K
    # i=first
    # j=last
    # while i<j:
    #     while(a[i]<k):i+=1
    #     while(a[j]>k):j-=1
    #     if(i<=j):
    #         swap(a[i],a[j])
    #         i+=1
    #         j-=1
        
    # #ex  1 4 3 2 3 8 7 6
    # # K=3
    #     i=0 thoa man => tiep tuc while
    #     i=1 arr[4]>=3 => dung while i 

    #     j=7,6,5 => thoa man
    #     j=4 : arr[j]=K => dung while j
    #     #a[i],a[j]=a[j],a[i]
    #     => 1 3 3 2 4 8 7 6
    #     i+=1 = 2
    #     j-=1 = 3

    #     i=2 arr[i]==3==K => dung while
    #     j=3 arr[j]=2 <k => dung while

    #     swap(a[i],a[j]) => 1 3 2     3 4 8 7 6
    #     i+=1 =3
    #     j+=1 =2 

    #     i>j => dung while tổng 
    #     => Nhận xét 
    #         i=3
    #         j=2
        
    #     => xảy ra:
    #         i==j==5
    #         i+1 = 6
    #         j-1 = 4
    #         => chắc chắn thằng 5 đúng vị trí 
    #         => sắp xếp first ,4   và 6 đến last 
            






