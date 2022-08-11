#%%
import turtle
import math
import cv2
turtle.Screen();
p= turtle.Turtle()
#turtle.bgcolor('blue')
p.speed(5)
p.penup()
p.goto(-300,0)
p.down();
p.fillcolor('yellow');p.begin_fill();
#ve ngoi nha hinh chu nhat
house_cdai = float(input('Nhap chieu dai ngoi nha: '))
house_crong = float(input('Nhap chieu rong ngoi nha: '))
for i in range (2):
    p.fd(house_crong)
    p.right(90)
    p.fd(house_cdai)
    p.right(90)
p.end_fill();
   
#ve mai nha hinh tam giac can
roof_cdai = house_crong
p.fillcolor('red');p.begin_fill();
p.lt(60)
p.fd(roof_cdai)
p.right(120)
p.fd(roof_cdai)
p.rt(10)
p.end_fill();

#ve cua chinh hcn
#a1=-250; a2=-300;
#b1=-150; b2=-300;
#c1=-250; c2=-150;
#d1=-150; d2=-150;
a_x = float(input('Nhap toa do diem Ax _door: '))
a_y = float(input('Nhap toa do diem Ay _door: '))
b_x = float(input('Nhap toa do diem Bx _door: '))
b_y = float(input('Nhap toa do diem By _door: '))
c_x = float(input('Nhap toa do diem Cx _door: '))
c_y = float(input('Nhap toa do diem Cy _door: '))
d_x = float(input('Nhap toa do diem Dx _door: '))
d_y = float(input('Nhap toa do diem Dy _door: '))
p.penup()
p.goto(a_x, a_y)
p.pendown(); p.fillcolor('blue');
p.begin_fill();
p.lt(90)
p.goto(c_x, c_y)
p.rt(90)
p.goto(d_x, d_y)
p.rt(90)
p.goto(b_x, b_y)
p.end_fill();

#ve cay

p.penup()
p.goto(0,0)
p.lt(100)
p.fd(300)
p.lt(150) 
p.fd(150)
p.rt(90)
p.pendown()  
p.fillcolor('brown');
p.begin_fill();
tree_cdai = float(input('Nhap chieu dai than cay:'))
tree_crong = float(input('Nhap chieu rong than cay:'))
for i in range (2): #ve than cay
    p.fd(tree_crong);
    p.rt(90);
    p.fd(tree_cdai);
    p.rt(90);
p.end_fill();
    
    #ve tan cay duoi
p.fillcolor('green');
p.begin_fill();
leaf_right = float(input('Nhap canh ben tan cay:'))
p.lt(180); p.fd((leaf_right- tree_crong)/2 ); #ve canh duoi la cay
p.rt(120); p.fd(leaf_right); #ve canh trai la cay
p.rt(120); p.fd(leaf_right); #ve canh phai la cay
p.rt(120); p.fd((leaf_right- tree_crong)/2); #ve canh duoi la cay  
p.end_fill();

    #ve tan cay tren
leaf_high = (leaf_right/2)* math.sqrt(3)
p.penup();
p.fd(tree_crong/2); p.rt(90);
p.fd(leaf_high); p.lt(90);
p.pd();p.fillcolor('green')
p.begin_fill();

p.fd(leaf_right/2); p.rt(120);
for i in range (2):
    p.fd(leaf_right); p.rt(120);
p.fd(leaf_right/2);
p.end_fill();

#ve mat troi
sun = float(input('Nhap ban kinh mat troi: '))
p.penup();
p.rt(90); p.fd(300);
p.pd(); p.fillcolor('red')
p.begin_fill()
p.circle(sun);
p.end_fill();


 
turtle.done();
#cv2.waitKey(10)
    # %%
