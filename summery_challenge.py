choice = "-"
while choice != "0":
    if choice in "12345":
        print("you choose {}".format(choice))
    else:
        print("please choose your options from the list below:")
        print("1.\tLearn python")
        print("2.\tLearn java")
        print("3.\tGo swimming")
        print("4.\tHave dinner")
        print("5.\tGo to bed")
        print("0.\tExit")
    choice = input()