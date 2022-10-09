from pydoc import plain
import random
import time

while True:
    print("Let's Go!")
    
    curr_num =1
    # luot choi 
    if random.randint(0,1)==0:
        curr_player = "A"
    curr_player = "B"
    
    while curr_num <=21:
        print("The current number is {}".format(curr_num), end="\n")
        
        if curr_player == "A":
            choices_A = int(input("Chon 1, 2 or 3: "))
            while choices_A not in [1,2,3]:
                print("KHONG HOP LE!")
                choices_A = int(input("Chon 1, 2 or 3: "))
            curr_num += choices_A
             
            if curr_num >=21:
                print("The currunt number is {}".format(curr_num))
                print("You lose")   
                break
            curr_player = "B"
            
        else:
            choices_B = random.randint(1,3)
            curr_num += choices_B
            print("B choices {}".format(choices_B))
            time.sleep(1)
            
            if curr_num>=21:
                print("The currunt number is {}".format(curr_num))
                print("You Win!")   
                break
            curr_player = "A"
            
    play_again = input("DO you want to play again! Yes click 1. No click 0")
    if play_again ==1:
        continue
    else:
        print("Bye")
        break