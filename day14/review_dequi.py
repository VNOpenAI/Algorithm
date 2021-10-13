# Đệ qui là hàm gọi đến chính nó
# Về bài tập đệ qui :  
    # Chia để trị : chia bài thành các bài toán con rồi dựa vào kết quả bài toán con => kết quả bài toán cha
        # Định nghĩa chức năng hàm thì thường là chức năng bài toán, ví dụ tính a mũ n thì gọi pow(a,n) : là a^n
        # Định nghĩa các neo , điểm dừng : n==1 => return a, n==0 return 1
        # Xác định bài toán con và tìm mối liên hệ giữa bài toán cha và bài toán con 
            # ví dụ :
                    # bài toán con là pow(a,n-1)  => mối liên hệ pow(a,n)=pow(a,n-1)*a
                    # bài toán con là pow(a,n//2) => mối liên hệ pow(a,n//2)..
        
        
    # Backtracking : 
        #chia làm 2 loại:
            # 1 : cố định đầu ra của output
            # 2 : không cố định đầu ra

        # ví dụ backtracking:
            #ví dụ 1: 
                #a) sinh ra số có k chữ số từ 1->M (các số có thể trùng nhau ví dụ k=3,m=5 =>111,123 )
                #b) sinh ra số có k chữ số từ 0->M (các số có thể trùng nhau ví dụ k=3,m=5 =>100)   
                    # thêm điều kiện if((i==0 and j!=0) or i!=0)
                    # xét a[0]:1->M gọi backtracking từ i=1
                #c) sinh ra số có số chữ số nhỏ hơn M từ các chữ số từ 1->M (các số cỏ thể trùng nhau):
                    # cứ đẩy j vào thì gọi output
                #d) sinh ra số có k chữ số từ 1->M (các số không  thể trùng nhau ví dụ k=3,m=5 =>123)
                    # cần mảng đánh dấu chú ý trả đánh dấu khi mà không khi không lấy phần tử đấy nữa
                #e) sinh ra số có k chữ số từ 1->M (chữ số sau lớn hơn chữ số trước)
                    # kiểm tra trùng ( đánh dấu ) + kiểm tra j>a[i-1] 

                #f)  
