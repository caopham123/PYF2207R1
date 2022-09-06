#%%
import math

a,b,c = 4,3,5
C = a+b+c 
print(C)
#%%
import math
a,b,c = 4,3,5
x= max(a,b,c)
y= min(a,b,c)
print(x, y)
# %%
a=2000
print(2022-a)

# %%
import math
pro_num = int(input('Nhap so sp'))
page_num = int(input('Nhap so sp'))
kq = math.ceil(pro_num/page_num)
print(kq)

# %%
import turtle
import math
p= turtle.Turtle()
#num = int(input('Nhap so hinh vuong'))
size = int(input('Nhap kich thuoc'))
dis = int(input('Nhap khoang cach'))
p.goto(0,0)
p.fd(size)
p.rt(90)
p.fd(size)
p.rt(90)
p.fd(size)
p.rt(90)
p.fd(size)
p.rt(90)
p.penup()

p.goto(size+dis,0)
p.pendown()
p.fd(size)
p.rt(90)
p.fd(size)
p.rt(90)
p.fd(size)
p.rt(90)
p.fd(size)
p.rt(90)

p.penup()
p.goto(2*(size+dis),0)
p.pendown()
p.fd(size)
p.rt(90)
p.fd(size)
p.rt(90)
p.fd(size)
p.rt(90)
p.fd(size)
p.rt(90)
turtle.done()
# %%
chuoi = 'JaSonAy'
chuoi_dau = len(chuoi)//2-1 #chia lay phan nguyen
chuoi_cuoi = len(chuoi)//2+2
print(chuoi[chuoi_dau:chuoi_cuoi])

#%%
password = 'abcd'
n = len(password)
p2 = password.replace(password[0:n+1:1],'*')
print(password[0:n+1:1])
print(p2)

# %%
####Commit 06.09 3:30