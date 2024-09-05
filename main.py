import random

uscore = 0
cscore = 0
options = ["rock", "paper", "scissor"]

while True:
    user_input = input("Choose rock/paper/scissor or Q to quit: ").lower()
    if user_input == "q":
        print(f"You score {uscore}")
        print(f"Computer score {cscore}")

        quit()
    if user_input not in options:
        continue
    
    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print(f"Computer chose {computer_pick}")
    
    if user_input == computer_pick:
        print("It's a tie!")
    elif (user_input == "rock" and computer_pick == "scissor") or \
        (user_input == "paper" and computer_pick == "rock") or \
        (user_input == "scissor" and computer_pick == "paper"):
        print("You won!!!")
        uscore += 1
    else:
        print("You lost!!!")
        cscore += 1
