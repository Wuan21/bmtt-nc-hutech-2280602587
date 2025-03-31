def tinh_tong_so_chan(n):
    tong = 0
    for num in lst:
        if num % 2 == 0:
            tong += num
    return tong

#nhap danh sach tong tu nguoi dung
input_list = input("Nhap danh sach cac so nguyen cach nhau boi dau phay: ")
numbers = list (map(int, input_list.split(',')))

#su dung ham va in ket qua
tong_chan = tinh_tong_so_chan(numbers)
print(f"Tong cac so chan trong danh sach la: {tong_chan}")
