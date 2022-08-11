#%%
import turtle
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
for i in range (2):
    p.fd(200)
    p.right(90)
    p.fd(300)
    p.right(90)
p.end_fill();
   
#ve mai nha hinh tam giac can
p.fillcolor('red');p.begin_fill();
p.lt(60)
p.fd(200)
p.right(120)
p.fd(200)
p.rt(10)
p.end_fill();
#ve cua chinh hcn
a1=-250; a2=-300;
b1=-150; b2=-300;
c1=-250; c2=-150;
d1=-150; d2=-150;
p.penup()
p.goto(a1,a2)
p.pendown(); p.fillcolor('blue');
p.begin_fill();
p.lt(90)
p.goto(c1,c2)
p.rt(90)
p.goto(d1,d2)
p.rt(90)
p.goto(b1,b2)
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
for i in range (2): #ve than cay
    p.fd(20);
    p.rt(90);
    p.fd(70);
    p.rt(90);
p.end_fill();
    
    #ve tan cay duoi
p.fillcolor('green');
p.begin_fill();
p.lt(180); p.fd(30); #ve canh duoi la cay
p.rt(120); p.fd(80); #ve canh trai la cay
p.rt(120); p.fd(80); #ve canh phai la cay
p.rt(120); p.fd(30); #ve canh duoi la cay  
p.end_fill();

    #ve tan cay tren
p.penup();
p.fd(10); p.rt(90);
p.fd(70); p.lt(90);
p.pd();p.fillcolor('green')
p.begin_fill();
p.fd(40); p.rt(120);
p.fd(80); p.rt(120);
p.fd(80); p.rt(120);
p.fd(40);
p.end_fill();

#ve mat troi
p.penup();
p.rt(90); p.fd(300);
p.pd(); p.fillcolor('red')
p.begin_fill()
p.circle(30);
p.end_fill();


 
turtle.done();
#cv2.waitKey(10)
    # %%
