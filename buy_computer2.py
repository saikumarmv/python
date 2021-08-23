available_parts = ["computer",
                   "monitor",
                   "key board",
                   "mouse",
                   "hdmi cable"
                   ]
current_choice = "_"
computer_parts = []  # create an empty list
# valid_choices = [str(i) for i in range(1, len(available_parts) + 1)]
valid_choices = []
for i in range(1, len(available_parts) + 1):
    valid_choices.append(str(i))
while current_choice != '0':
    if current_choice in valid_choices:
        print("adding {}".format(current_choice))
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        computer_parts.append(chosen_part)

    else:
        print("please add the options from the list below:")
        # for part in available_parts:
        for number, part in enumerate(available_parts):
            print("{0}:  {1}".format(number + 1, part))
        print("0 : to exit")
    current_choice = input()
print(computer_parts)
