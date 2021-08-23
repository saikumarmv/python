parrot = "Norwegian blue"

letter = input(" enter a character :")

if letter in parrot:
    print("{} s in {}".format(letter, parrot))
else:
    print("i don't need that letter")
