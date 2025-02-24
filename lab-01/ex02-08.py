#Ham kiem tra so nhi phan co chia het cho 5 ko
def chia_het_cho_5(so_nhi_phan):
    #chuyen so nhi phan sang so thap phan
    so_thap_phan = int(so_nhi_phan, 2)
    #kiem tra so thap phan co chia het cho 5 ko
    if so_thap_phan % 5 == 0:
        return True
    else:
        return False
#Nhap so tu nguoi dung
chuoi_so_nhi_phan = input("Nhap so nhi phan: ")
#tach chuoi thanh cac so nhi phan va ktra chia het cho 5
so_nhi_phan_list = chuoi_so_nhi_phan.split(',')
so_chia_het_cho_5 = [so for so in so_nhi_phan_list if chia_het_cho_5(so)]
#in ra cac so nhi phan chia het cho 5
if len(so_chia_het_cho_5) > 0:
    ket_qua = ','.join(so_chia_het_cho_5)
    print("Cac so nhi phan chia het cho 5 la: ", ket_qua)
else:
    print('Khong co so nao chia het cho 5')