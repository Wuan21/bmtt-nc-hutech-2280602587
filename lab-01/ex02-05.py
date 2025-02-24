so_gio_lam = float(input("Nhap so gio lam viec moi tuan: "))
luong_gio = float(input("Nhap luong moi gio: "))
gio_tieu_chuan = 44 #kpi gio lam moi tuan.
gio_vuot_chuan = max(0, so_gio_lam - gio_tieu_chuan) #so gio vuot chuan
luong_nhan_duoc = gio_tieu_chuan * luong_gio + gio_vuot_chuan * luong_gio * 1.5
print (f"Luong nhan duoc cua nv la: {luong_nhan_duoc}")