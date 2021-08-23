for i in range(1, 13):
    for j in range(1, 13):
        print("{1:^2} * {0:^3} = {2:^3}  |".format(j, i, i * j))
    print("-" * 17)
