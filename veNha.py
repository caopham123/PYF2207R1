import re
import turtle as tl

sceen= tl.Screen()
sceen.title="Ve Nha"
pen = tl.Turtle()
pen.penup()
pen.goto(x=-100, y= -200)
pen.pendown()

def input_Room():
    h_height = int(input("Nhap chieu cao phong: "))
    h_width = int(input("Nhap chieu rong phong: "))
    #h_num = int(input("Nhap so phong: "))
    return h_height, h_width


  
def build_room(h_height, h_width):
    #input_Room()
    pen.fillcolor("red")
    pen.begin_fill()
    for i in range (2):
        pen.fd(h_width)
        pen.lt(90)
        pen.fd(h_height)
        pen.lt(90)
    pen.fd(h_width)
    pen.end_fill()

##      
def input_floor():
    room_num = int(input("Nhap so phong: "))
    while room_num <0 or room_num >10:
        print("Khong hop le. Nhap lai: ")
        room_num = int(input("Nhap so phong: "))
    return room_num
    

def Main():
    #input_Room()
    #input_floor()
    h,w = input_Room()
    
    room_num = input_floor()
    
    ##build house
    for i in range (room_num):
        build_room(h,w)
    
Main()
    

