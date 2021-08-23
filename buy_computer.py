available_parts = ["computer",
                   "monitor",
                   "key board",
                   "mouse",
                   "mouse pad",
                   "hdmi cable"
                   ]
current_choice = "_"
computer_parts = []  # create an empty list
while current_choice != '0':
    if current_choice in "123456:":
        print("adding {}".format(current_choice))
        if current_choice == "1":
            computer_parts.append("computer")
        elif current_choice == "2":
            computer_parts.append("monitor")
        elif current_choice == "3":
            computer_parts.append("keyboard")
        elif current_choice == "4":
            computer_parts.append("mouse")
        elif current_choice == "5":
            computer_parts.append("mouse mat")
        elif current_choice == "6":
            computer_parts.append("hdmi cable")
    else:
        print("please add the options from the list below:")
        # for part in available_parts:
        for number, part in enumerate(available_parts):
            print("{0}:  {1}".format(number+ 1, part))
        print("0 : to exit")
    current_choice = input()
print(computer_parts)
