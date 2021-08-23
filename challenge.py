name = input(" enter name:\n")
age = int(input(" how old are you?"))
if 18 <= age < 31:
    print("welcome to the club holidays (18 - 30), {}".format(name))
else:
    print("get out from here ")