print("SNAKE_WATER_GUN")
humanPoint = 0
computerPoint = 0
i = 9
while i >= 1:
    import random

    lst = ["s", "w", "g"]
    choice = random.choice(lst)
    a = (input("s for Snake \nw for Water \ng for Gun \nEnter your choice: "))
    print(choice)
    if a == choice:
        print("DRAW")
    elif a == "s" and choice == "w":
        print("You_win.")
        human_point += 1
    elif a == "s" and choice == "g":
        print("You_lose.")
        computer_point += 1
    elif a == "w" and chice == "s":
        print("You_lose.")
        computer_point += 1
    elif a == "w" and choice == "g":
        print("You_win.")
        human_point += 1
    elif a == "g" and choice == "s":
        print("You_win.")
        human_point += 1
    elif a == "g" and choice == "w":
        print("You_lose.")
        computer_point += 1
    else:
        print("Please_type_valid_input.")

    print(f"{i} chances are left out of 10")
    i -= 1

print(human_point)
print(computer_point)
if human_point > computer_point:
    print("YOU WIN THIS GAME.")
elif human_point == computer_point:
    print("THE GAME IS DRAW. \nPlay agian.")
else:
    print("YOU LOSE THIS GAME.")
