import turtle as tl

sceen= tl.Screen()
pen= tl.Turtle()
pen.speed(5)
number = int(input("Nhap so luong hinh tron: "))
r = int(input("Nhap ban kinh hinh tron: "))
for i in range(number):
    pen.circle(r)
    pen.right(50)
    
pen.screen.mainloop()
    
