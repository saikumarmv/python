
number = input("please enter a seres of numbers using seperatoers you like:\n")
seperators = ""
for char in number:
    if not char.isnumeric():
        seperators = seperators + char
print(seperators)
values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])
values = "".join(char if char not in seperators else " " for char in number).split()
print(sum(int(val) for val in values))