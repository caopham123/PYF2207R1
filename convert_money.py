import imp


import math
usd = float(input('Nhap so tien can doi: '))
ty_gia = float(input('Ty gia USD/VN: '))
vnd = usd* ty_gia*1000
print('==> Chuyen doi thanh {} VND'.format(vnd))