#tao 1 danh sach rong de luu kqua
j=[]
#duyet qua so trong doan tu 2000-3200, kiem tra xem co chia het cho 7 va ko phai la boi cua so 5 ko
for i in range(2000, 3201):
    if (i % 7 == 0) and  (i % 5 != 0):
        j.append(str(i))
        print(','.join(j))