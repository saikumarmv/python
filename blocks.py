for i in range(1, 13):
    print("no. {} squre is {} and cubed is {:4}".format(i, i ** 2, i ** 3))
name = input(" plead anter the name\n")
age = int(input("how old ae you,{0}?".format(name)))
print(age)
# if age >= 18:
#     print("you are old enough to vote")
#     print("please put your vote in the box")
# else:
#     print("please comeback after {} years".format(18-age))
if age < 18:
    print("please comeback after {} years".format(18-age))
elif age>=101:
    print("sorry you are out of range of human life")
else:
    print("you are old enough to vote")
    print("please p00000000000000000ut your vote in the box")