for i in range(1,13):
    print("no.{0:2} squared is {1:4} and cubed is {2:4}".format(i,i**2,i**3))

print()

for i in range(1,13):
    print("no.{0:2} squared is {1:<4} and cubed is {2:^4}".format(i,i**2,i**3))


print()
print("pi is approximately {0:12}".format(22 / 7))
print("pi is approximately {0:12f}".format(22 / 7))

print("pi is approximately {0:12.50f}".format(22 / 7))
print("pi is approximately {0:12}".format(22 / 7))