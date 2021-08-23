available_exits = ["north", "south", "east", "west"]
choosen_exit = ""
while choosen_exit not in available_exits:
    choosen_exit = input("please choose drection:\n")
    if choosen_exit.casefold() == "quit":
        print("game over")
        break
else:
    print("aren't you glad you got out of there")
