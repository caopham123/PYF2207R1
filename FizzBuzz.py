number = int(input('Nhap so1: '))
number1 = int(input('Nhap so2: '))
while (number<=0 & number>=number1):
    print('Nhap lai!')
    number = int(input('Nhap so1: '))
    number1 = int(input('Nhap so2: '))

for i in range (number, number1+1, 1):
    
    if(i %3==0 & i%5==0):
        print('FizzBuzz',i)
    elif(i %5==0):
        print('Buzz', i)
    elif(i %3==0):
        print('Fizz', i)
    else:
        pass

