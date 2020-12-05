import random
while True:
    print("---WELCOME TO NUMBER GUESS GAME---")
    lives=5
    number=random.randint(1,99)
    while True:
        print(20*"-")
        print("live: ",lives)
        guess=int(input("ENTER AN INTEGER FROM 1 TO 99: "))
        if lives == 1:
            print("<<<<<GAME OVER>>>>>\n")
            break
        elif guess>number:
            print("guess is high")
            lives-=1
        elif guess<number:
            print("guess is low")
            lives-=1
        elif guess<number:
            print(f"CONGRATULATIONS GUESS IS {number}")
            break



        


        
