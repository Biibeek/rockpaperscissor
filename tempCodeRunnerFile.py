import random
uscore=0
cscore=0
options=["rock","paper","scissor"]
while True:
    user_input=input("choose rock/paper/scissor or Q to quit:").lower()
    if user_input=="q":
        break
    if user_input not in options:
        continue
    random_number=random.randint(0,2)
    computer_pick=options[random_number]
    print(f"Computer chose {computer_pick}")
    if user_input == computer_pick:
        print("It's a tie!")
        
    if user_input=="rock" and computer_pick=="scissor":
        print("you won!!!")
        uscore +=1
    elif user_input=="paper" and computer_pick=="rock":
        print("you won!!!")
        uscore +=1
    elif user_input=="scissor" and computer_pick=="paper":
        print("you won!!!")
        uscore +=1
    else:
        print("you lost!!!")
        cscore +=1
print(f"you won with score {uscore}")
print(f"computer won with score {cscore}")